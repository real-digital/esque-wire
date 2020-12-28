import asyncio
import shutil
import tempfile
import threading
from contextlib import closing
from pathlib import Path
from typing import List, Optional, Union

from tests.cluster_fixture.base import DEFAULT_KAFKA_VERSION, KafkaVersion, get_loop
from tests.cluster_fixture.kafka import Endpoint, KafkaInstance, PlaintextEndpoint, SaslMechanism
from tests.cluster_fixture.zookeeper import ZookeeperInstance


class Cluster:
    def __init__(
        self,
        cluster_id: int = 1,
        cluster_size: int = 1,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        endpoints: Optional[List[Endpoint]] = None,
        sasl_mechanisms: Optional[List[SaslMechanism]] = None,
        keep_temporary_files: bool = False,
    ):
        """
        This class will create and manage all resources required to start up and monitor a Kafka cluster.

            >>> from tests.cluster_fixture import Cluster
            >>> with Cluster() as cluster:
            ...    print(cluster.get_bootstrap_servers("PLAINTEXT"))
            ['PLAINTEXT://localhost:9092']

        :param cluster_id: Used for naming the control thread and working directory for this cluster.
        :param cluster_size: Used to set how many brokers should be started.
        :param kafka_version: The kafka version the brokers should use.
        :param working_directory: The working directory containing all configuration files for Kafka and Zookeeper.
                                  Defaults to a temporary directory if `None`.
        :param endpoints: The list of get_endpoints each broker within the cluster should have. Can all use the same
                          ports, free ports will be determined during startup. Defaults to just a single plaintext
                          endpoint if `None`.
        :param sasl_mechanisms: The list of sasl mechanisms the broker shall support. Defaults to `["PLAIN"]` if `None`.
        :param keep_temporary_files: Determines whether to keep or delete the working directory after shutdown.
        """
        self._cluster_size = cluster_size
        self._components: List[Union[ZookeeperInstance, KafkaInstance]] = []
        self._exception: Optional[Exception] = None
        self._kafka_version = kafka_version
        self._keep_temporary_files = keep_temporary_files
        self._sasl_mechanisms = sasl_mechanisms
        self._shutdown = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self.brokers: List[KafkaInstance] = []
        self.cluster_id = cluster_id
        self.shutdown_complete = threading.Event()
        self.startup_complete = threading.Event()
        self.zk_instance: Optional[ZookeeperInstance] = None

        if working_directory is None:
            working_directory = Path(tempfile.mkdtemp(prefix="kafka_fixture_")) / f"cluster{cluster_id:02}"
        self._working_directory = working_directory

        if endpoints is None:
            endpoints = [PlaintextEndpoint()]

        self._endpoints: List[Endpoint] = endpoints
        # make sure get_endpoints don't use same ports
        if len({ep.port for ep in self._endpoints}) != len(self._endpoints):
            first_port = self._endpoints[0].port
            self._endpoints = [ep.with_port(first_port + i) for i, ep in enumerate(self._endpoints)]

    def start(self) -> None:
        """
        Start the cluster after it has been created or stopped.
        If this cluster is used as a contextmanager, this function will automatically be called.
        When restarting a stopped cluster, the ports are only guaranteed to stay the same if nothing
        else has bound to them in the meantime.

            >>> cluster = Cluster()
            >>> try:
            ...     cluster.start()
            ...     print(cluster.get_bootstrap_servers("PLAINTEXT"))
            ... finally:
            ...     cluster.stop()
            ['PLAINTEXT://localhost:9092']
            >>> # try-finally construct omitted here for brevity.
            >>> cluster.start()
            >>> print(cluster.get_bootstrap_servers("PLAINTEXT"))
            ['PLAINTEXT://localhost:9092']
            >>> cluster.close()

        :raises RuntimeError: When called on a cluster that is running.
        """
        self.start_nowait()
        self.startup_complete.wait()
        if self._exception:
            raise self._exception

    def start_nowait(self) -> None:
        """
        Non-blocking version of :meth:`start`. Use :attr:`startup_complete` to determine if the cluster has completed
        startup.
        """
        if self._thread is not None:
            raise RuntimeError("Cluster already running or not properly closed!")
        self.startup_complete.clear()
        self.shutdown_complete.clear()
        self._shutdown.clear()
        self._components.clear()
        self.brokers.clear()
        self.zk_instance = None
        self._exception = None
        self._thread = threading.Thread(name=f"Cluster{self.cluster_id:02}EventLoop", target=self._run)
        self._thread.start()

    def _run(self) -> None:
        with closing(get_loop()) as loop:
            self.zk_instance = ZookeeperInstance(
                kafka_version=self._kafka_version, working_directory=self._working_directory / "zookeeper", loop=loop
            )

            self.brokers.extend(
                KafkaInstance(
                    broker_id=broker_id,
                    zookeeper_instance=self.zk_instance,
                    cluster_size=self._cluster_size,
                    kafka_version=self._kafka_version,
                    working_directory=self._working_directory / f"broker{broker_id:02}",
                    loop=loop,
                    endpoints=self._endpoints,
                    sasl_mechanisms=self._sasl_mechanisms,
                )
                for broker_id in range(self._cluster_size)
            )
            self._components.extend(self.brokers)
            self._components.append(self.zk_instance)

            all_done = asyncio.gather(*(comp.start_async() for comp in self._components), return_exceptions=True)
            results = loop.run_until_complete(all_done)
            for result in results:
                if isinstance(result, Exception):
                    self._exception = result
                    self._shutdown.set()
                    break
            self.startup_complete.set()
            loop.run_until_complete(self._check_shutdown())

    async def _check_shutdown(self) -> None:
        while not self._shutdown.is_set():
            await asyncio.sleep(0.1)

        results = await asyncio.gather(*(comp.close_async() for comp in self._components), return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                self._exception = result
                break
        self.shutdown_complete.set()

    def stop(self) -> None:
        """
        Stop a running cluster, does nothing if the cluster is inactive.
        See :meth:`start` for usage example.
        """
        if self._thread is None:
            # got stopped before it even started, nothing to do
            return
        self._shutdown.set()
        self._thread.join()
        self._thread = None
        if self._exception:
            exc = self._exception
            self._exception = None
            raise exc

    def close(self) -> None:
        """
        Close the cluster. Basically does the same as :meth:`stop` but will also remove the working directory if
        requested.
        """
        self.stop()
        if not self._keep_temporary_files and self._working_directory.exists():
            shutil.rmtree(self._working_directory)

    def get_bootstrap_servers(self, listener_name: str = "PLAINTEXT") -> List[str]:
        """
        Retrieve the first **up to three** endpoint urls for the given `listener_name`.

        Keep in mind that this is not necessarily the same as the security protocol.
        For more information about `security_protocol` vs `listener_name` see :class:`Endpoint`.

        :param listener_name: The name of the get_endpoints which shall be retrieved.
        :return: A list of endpoint urls in the form `security_protocol://host:port`
                 e.g. `["PLAINTEXT://localhost:9092"]`.
        :raises RuntimeError: If the cluster is not running.
        :raises KeyError: If there is no listener with the given name on one or more brokers.
        """
        self.assert_running()
        return [broker.get_endpoint_url(listener_name) for broker in self.brokers[:3]]

    def get_endpoints(self, listener_name: str = "PLAINTEXT") -> List[Endpoint]:
        """
        Retrieve all brokers' :class:`Endpoint` objects for the given `listener_name`.

        Keep in mind that the `listener_name` is not necessarily the same as the security protocol.
        For more information about `security_protocol` vs `listener_name` see :class:`Endpoint`.

        :param listener_name: The name of the get_endpoints which shall be retrieved.
        :return: A list of :class:`Endpoint` with the given `listener_name`.
        :raises RuntimeError: If the cluster is not running.
        :raises KeyError: If there is no listener with the given name on one or more brokers.
        """
        self.assert_running()
        return [broker.get_endpoint(listener_name) for broker in self.brokers]

    @property
    def zookeeper_url(self) -> str:
        """
        Retrieve the url of the zookeeper instance that's running for this cluster.

        :return: The zookeeper url in the form `host:port`, e.g. `"localhost:8081"`.
        :raises RuntimeError: If the cluster is not running.
        """
        self.assert_running()
        assert self.zk_instance is not None
        return self.zk_instance.url

    def assert_running(self) -> None:
        """
        Make sure the cluster is running.

        :raises RuntimeError: If the cluster is not running.
        """
        if self._thread is None:
            raise RuntimeError("Cluster hasn't been started yet!")
        if not self.startup_complete.is_set():
            raise RuntimeError("Cluster startup is not complete!")
        if self.shutdown_complete.is_set():
            raise RuntimeError("Cluster is shut down!")
        if not self._thread.is_alive():
            raise RuntimeError("Cluster thread has died!")

    def __enter__(self) -> "Cluster":
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
