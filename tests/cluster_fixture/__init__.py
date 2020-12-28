import asyncio
import logging
import shutil
import tempfile
import threading
from contextlib import closing
from pathlib import Path
from typing import List, Optional, Union

from tests.cluster_fixture.base import DEFAULT_KAFKA_VERSION, KafkaVersion, get_loop
from tests.cluster_fixture.kafka import Endpoint, KafkaInstance, PlaintextEndpoint, SaslMechanism
from tests.cluster_fixture.zookeeper import ZookeeperInstance

logger = logging.getLogger(__name__)


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
        self.cluster_id = cluster_id
        self.startup_complete = threading.Event()
        self.shutdown_complete = threading.Event()
        self._shutdown = threading.Event()
        self._cluster_size = cluster_size
        self._kafka_version = kafka_version
        self._sasl_mechanisms = sasl_mechanisms
        self._thread: Optional[threading.Thread] = None
        self.zk_instance: Optional[ZookeeperInstance] = None
        self.brokers: List[KafkaInstance] = []
        self._components: List[Union[ZookeeperInstance, KafkaInstance]] = []
        self._exception: Optional[Exception] = None
        self._keep_temporary_files = keep_temporary_files

        if working_directory is None:
            working_directory = Path(tempfile.mkdtemp(prefix="kafka_fixture_")) / f"cluster{cluster_id:02}"
        self._working_directory = working_directory

        if endpoints is None:
            endpoints = [PlaintextEndpoint()]

        self._endpoints: List[Endpoint] = endpoints
        # make sure endpoints don't use same ports
        if len({ep.port for ep in self._endpoints}) != len(self._endpoints):
            first_port = self._endpoints[0].port
            self._endpoints = [ep.with_port(first_port + i) for i, ep in enumerate(self._endpoints)]

    def start(self) -> None:
        self.start_nowait()
        self.startup_complete.wait()
        if self._exception:
            raise self._exception

    def start_nowait(self) -> None:
        if self._thread is not None:
            raise RuntimeError("Cluster already running or not properly closed!")
        self.startup_complete.clear()
        self.shutdown_complete.clear()
        self._shutdown.clear()
        self._components.clear()
        self.brokers.clear()
        self.zk_instance = None
        self._exception = None
        self._thread = threading.Thread(name=f"Cluster{self.cluster_id:02}EventLoop", target=self.run)
        self._thread.start()

    def run(self) -> None:
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
            loop.run_until_complete(self.check_shutdown())

    async def check_shutdown(self) -> None:
        while not self._shutdown.is_set():
            await asyncio.sleep(0.1)

        all_done = asyncio.gather(*(comp.close_async() for comp in self._components))
        try:
            await all_done
        except Exception as e:
            self._exception = e
        self.shutdown_complete.set()

    def stop(self) -> None:
        self._shutdown.set()

    def close(self) -> None:
        if self._thread is None:
            # got closed before it even started, nothing to do
            return
        self.stop()
        self._thread.join()
        if self._exception:
            raise self._exception
        self._thread = None
        if not self._keep_temporary_files:
            shutil.rmtree(self._working_directory)

    def restart(self) -> None:
        tmp = self._keep_temporary_files
        self._keep_temporary_files = True
        self.close()
        self.start()
        self._keep_temporary_files = tmp

    def boostrap_servers(self, listener_name: str = "PLAINTEXT") -> List[str]:
        self.assert_running()
        return [broker.get_endpoint_url(listener_name) for broker in self.brokers[:3]]

    @property
    def zookeeper_url(self) -> str:
        self.assert_running()
        assert self.zk_instance is not None
        return self.zk_instance.url

    def assert_running(self) -> None:
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
