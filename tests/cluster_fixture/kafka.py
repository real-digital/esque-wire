import asyncio
import re
import socket
import ssl
import struct
from abc import ABC, abstractmethod
from asyncio.protocols import BaseProtocol
from asyncio.transports import BaseTransport
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Awaitable, List, Optional, Tuple, TypeVar

from tests.cluster_fixture.base import DEFAULT_KAFKA_VERSION, Component, KafkaVersion, get_jinja_env
from tests.cluster_fixture.zookeeper import ZookeeperInstance

if TYPE_CHECKING:
    from tests.cluster_fixture.cluster import Cluster

KAFKA_STARTUP_PATTERN = re.compile(r"\[KafkaServer id=\d+\] started \(kafka\.server\.KafkaServer\)")
CORR_ID: bytes = struct.pack(">i", 1337)
KAFKA_GENERIC_API_VERSION_REQUEST = (
    b"\x00\x00\x00\x16"  # message size
    b"\x00\x12"  # api_key 18 = api_versin request
    b"\x00\x00" + CORR_ID + b"\x00\x0c"  # api_version 0  # correlation ID  # length of client_id
    b"probe_client"  # client_id
)

E = TypeVar("E", bound="Endpoint")


class Endpoint(ABC):
    def __init__(self, name: Optional[str] = None, port: int = 9092):
        """
        Abstract endpoint that designates a port where kafka listens for connections.
        The endpoint's security protocol is determined by the subclass, the endpoint's name can be given when creating
        it.

        It is possible to have multiple get_endpoints providing the same access type (i.e. security protocol) under
        different ports if they use different names.

        :param name: Name for this endpoint, defaults to security protocol if not given.
        :param port: Desired port to start looking for free ports.
        """
        if name is None:
            self.listener_name = self.security_protocol
        else:
            self.listener_name = name
        self.port = port

    @property
    @abstractmethod
    def security_protocol(self) -> str:
        """
        Security protocol this endpoint serves.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def sasl_enabled(self) -> bool:
        """
        Whether this endpoint is secured with SASL or not.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def ssl_enabled(self) -> bool:
        """
        Whether this endpoint is secured with SASL or not.
        """
        raise NotImplementedError

    def with_incremented_port(self: E, offset: int) -> E:
        """
        Return a copy of this endpoint where the port is incremented by `offset`.

        :param offset: The offset to add to this endpoint's port to get the new endpoint.
        :returns: Copy of this endpoint with the port incremented by `offset`.
        """
        return self.with_port(self.port + offset)

    def with_port(self: E, port: int) -> E:
        """
        Return a copy of this endpoint where the port is set to `port`.

        :param port: The port number the new endpoint should have.
        :returns: Copy of this endpoint with the port set to `port`.
        """
        return type(self)(self.listener_name, port)

    @property
    def url(self) -> str:
        """
        The full url of this endpoint in the form `<security_protocol>://<host>:<port>`,
        e.g. `"PLAINTEXT://localhost:9092"`
        :returns: Url of this endpoint, e.g `"PLAINTEXT://localhost:9092"`.
        """
        return f"{self.security_protocol}://{self.address}"

    @property
    def address(self) -> str:
        """
        The address of this endpoint in the form `<host>:<port>`,
        e.g. `"localhost:9092"`
        :returns: Address of this endpoint, e.g `"localhost:9092"`.
        """
        return f"localhost:{self.port}"

    def copy(self: E) -> E:
        """
        Retrieve a copy of this object.

        :returns: Copy of this object.
        """
        return type(self)(self.listener_name, self.port)


class PlaintextEndpoint(Endpoint):
    """
    An endpoint that provides PLAINTEXT access to kafka.

        >>> from tests.cluster_fixture import Cluster, PlaintextEndpoint
        >>> with Cluster(endpoints=[PlaintextEndpoint("TEST")]) as cluster:
        ...    print(cluster.get_bootstrap_servers("TEST"))
        ['PLAINTEXT://localhost:9092']
    """

    @property
    def sasl_enabled(self):
        return False

    @property
    def ssl_enabled(self):
        return False

    @property
    def security_protocol(self) -> str:
        return "PLAINTEXT"


class SaslEndpoint(Endpoint):
    """
    An endpoint that provides SASL secured PLAINTEXT access to kafka.

        >>> from tests.cluster_fixture import Cluster, SaslEndpoint
        >>> with Cluster(endpoints=[SaslEndpoint("TEST")]) as cluster:
        ...    print(cluster.get_bootstrap_servers("TEST"))
        ['SASL_PLAINTEXT://localhost:9092']
    """

    @property
    def sasl_enabled(self):
        return True

    @property
    def ssl_enabled(self):
        return False

    @property
    def security_protocol(self) -> str:
        return "SASL_PLAINTEXT"


class SslEndpoint(Endpoint):
    """
    An endpoint that provides TLS secured access to kafka.

        >>> from tests.cluster_fixture import Cluster, SslEndpoint
        >>> with Cluster(endpoints=[SslEndpoint("TEST")]) as cluster:
        ...     print(cluster.get_bootstrap_servers("TEST"))
        ['SSL://localhost:9092']
    """

    @property
    def sasl_enabled(self) -> bool:
        return False

    @property
    def ssl_enabled(self):
        return True

    @property
    def security_protocol(self) -> str:
        return "SSL"


class SaslSslEndpoint(Endpoint):
    """
    An endpoint that provides TLS secured access to kafka.

    Note: SASL authentication takes precedence over SSL authentication.
    If you have `ssl.client.auth=required`, this endpoint will still require
    SASL authentication!

        >>> from tests.cluster_fixture import Cluster, SaslSslEndpoint
        >>> with Cluster(endpoints=[SaslSslEndpoint("TEST")]) as cluster:
        ...     print(cluster.get_bootstrap_servers("TEST"))
        ['SASL_SSL://localhost:9092']
    """

    @property
    def sasl_enabled(self) -> bool:
        return True

    @property
    def ssl_enabled(self):
        return True

    @property
    def security_protocol(self) -> str:
        return "SASL_SSL"


@dataclass
class SaslMechanism:
    """
    Holds the name of a SASL mechanism.
    For example `"PLAIN"` or `"SCRAM-SHA-512"`.
    """

    name: str


class KafkaInstance(Component):
    def __init__(
        self,
        cluster: "Cluster",
        broker_id: int,
        zookeeper_instance: ZookeeperInstance,
        cluster_size: int = 1,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        endpoints: Optional[List[Endpoint]] = None,
        sasl_mechanisms: Optional[List[SaslMechanism]] = None,
    ):
        """
        The broker component of a Kafka cluster. For more information see :class:`Component`.

        :param cluster: The cluster this broker belongs to.
        :param broker_id: The cluster-unique id of this broker.
        :param zookeeper_instance: The zookeeper instance that belongs to the cluster.
        :param cluster_size: The overall size of the cluster. Used to determine increments for port discovery.
        :param kafka_version: The kafka version the component should use.
        :param working_directory: The working directory containing all configuration files for this broker.
                                  Defaults to a temporary directory if `None`.
        :param loop: The asyncio event loop to use for communicating with the broker.
                     If `None` then the running loop within the active thread will be used or a new one will be created
                     if there is no running loop.
        :param endpoints: The list of get_endpoints this broker should provide.
        :param sasl_mechanisms: The list of sasl mechnisms this broker should support.
        """
        # set broker_id first so self.component_name can use it
        self.broker_id = broker_id
        self._cluster: "Cluster" = cluster
        super().__init__(kafka_version, working_directory, loop)

        if endpoints is None:
            endpoints = [PlaintextEndpoint()]
        if len(endpoints) == 0:
            raise ValueError("Cannot start without get_endpoints!")

        self.endpoints: List[Endpoint] = [e.with_incremented_port(broker_id * len(endpoints)) for e in endpoints]

        if sasl_mechanisms is None:
            if any(endpoint.sasl_enabled for endpoint in self.endpoints):
                self.sasl_mechanisms = [SaslMechanism("PLAIN")]
            else:
                self.sasl_mechanisms = []
        else:
            if any(endpoint.sasl_enabled for endpoint in self.endpoints) and len(sasl_mechanisms) == 0:
                raise ValueError("Need to define at least one sasl mechanism if secure endpoint is available!")
            self.sasl_mechanisms = sasl_mechanisms

        self._cluster_size = cluster_size
        self._zk_instance = zookeeper_instance
        self._zk_instance.register_broker(self)

    async def _start_async(self) -> None:
        self._logger.info("Waiting for zookeeper to complete startup")
        assert self._zk_instance.startup_complete, "Startup Task for zk instance has not been created!"
        await self._zk_instance.startup_complete
        await super()._start_async()

    @property
    def component_name(self) -> str:
        return f"broker{self.broker_id:02}"

    @property
    def zk_address(self) -> str:
        """
        Used within the config template to determine the zookeeper address to connect this broker to.
        """
        return self._zk_instance.url

    @property
    def data_dir(self) -> Path:
        """
        Used within the config template to determine the directory where the topic data is stored.
        """

        return self._working_directory / "data"

    @property
    def config_file(self) -> Path:
        """
        Path to this broker's main configuration file.
        """
        return self._working_directory / "server.properties"

    @property
    def sasl_config_file(self) -> Path:
        """
        Path to this broker's SASL configuration file. It holds all users and passwords for the PLAIN mechanism.
        """
        return self._working_directory / "sasl_jaas.conf"

    def get_endpoint_url(self, listener_name: str) -> str:
        """
        Retrieve the endpoint url for the given `listener_name`.

        Keep in mind that this is not necessarily the same as the security protocol.
        For more information about `security_protocol` vs `listener_name` see :class:`Endpoint`.

        :param listener_name: The name of the endpoint whose url shall be retrieved.
        :return: The url of the endpoint in the form `security_protocol://host:port`
                 e.g. `["PLAINTEXT://localhost:9092"]`.
        :raises KeyError: If there is no listener with the given name.
        """
        for e in self.endpoints:
            if e.listener_name == listener_name:
                break
        else:
            raise KeyError(listener_name)
        return e.url

    def get_endpoint(self, listener_name: str) -> Endpoint:
        """
        Retrieve all brokers' :class:`Endpoint` objects for the given `listener_name`.

        Keep in mind that the `listener_name` is not necessarily the same as the security protocol.
        For more information about `security_protocol` vs `listener_name` see :class:`Endpoint`.

        :param listener_name: The name of the get_endpoints which shall be retrieved.
        :return: A list of :class:`Endpoint` with the given `listener_name`.
        :raises KeyError: If there is no listener with the given name.
        """
        for e in self.endpoints:
            if e.listener_name == listener_name:
                break
        else:
            raise KeyError(listener_name)
        return e.copy()

    def _get_ports(self) -> List[int]:
        return [e.port for e in self.endpoints]

    def _increment_ports(self) -> None:
        for endpoint in self.endpoints:
            endpoint.port += self._cluster_size

    def _render_config(self) -> None:
        env = get_jinja_env()
        server_conf_template = env.get_template("server.properties.j2")
        sasl_conf_template = env.get_template("sasl_jaas.conf.j2")
        self.config_file.write_text(server_conf_template.render(broker=self, cluster=self._cluster))
        self.sasl_config_file.write_text(sasl_conf_template.render(broker=self, cluster=self._cluster))

    def _subprocess_exec(self) -> Awaitable[Tuple[BaseTransport, BaseProtocol]]:
        return self._loop.subprocess_exec(
            self._proto.get_self,
            str(self.bin_dir / "kafka-server-start.sh"),
            str(self.config_file),
            env={"KAFKA_OPTS": f"-Djava.security.auth.login.config={self.sasl_config_file}"},
        )

    async def probe_service(self) -> bool:
        # see if we can find an endpoint without ssl, since they're slightly faster to query
        for ep in self.endpoints:
            if not ep.ssl_enabled:
                response = await self._send_api_version_request_plain(ep.port)
                break
        else:
            # none found, so ssl it is...
            response = await self._send_api_version_request_ssl(self.endpoints[0].port)

        self._logger.debug(
            f"Requested api versions\nResponse length: {len(response)}\nResponse[:16]: {response[:16]!r}"
        )
        corr_id: bytes = response[:4]
        return corr_id == CORR_ID

    async def _send_api_version_request_plain(self, port: int) -> bytes:
        with closing(socket.socket(type=socket.SOCK_STREAM)) as sock:
            sock.setblocking(False)
            await self._loop.sock_connect(sock, ("localhost", port))
            await self._loop.sock_sendall(sock, KAFKA_GENERIC_API_VERSION_REQUEST)
            expected_bytes = struct.unpack(">i", await self._loop.sock_recv(sock, 4))[0]
            received_bytes = 0
            data = []
            while received_bytes < expected_bytes:
                data.append(await self._loop.sock_recv(sock, 1024))
                received_bytes += len(data[-1])
            sock.shutdown(socket.SHUT_RDWR)

        return b"".join(data)

    async def _send_api_version_request_ssl(self, port: int) -> bytes:
        ssl_ctx = ssl.create_default_context(
            ssl.Purpose.SERVER_AUTH, cafile=str(self._cluster.ssl_server_cert_location)
        )
        if self._cluster.ssl_client_auth_enabled:
            ssl_ctx.load_cert_chain(
                certfile=self._cluster.ssl_client_cert_location, keyfile=self._cluster.ssl_client_key_location
            )

        # The event loop's sock_recv function doesn't support ssl sockets.
        # See: https://stackoverflow.com/a/56775511/2677943
        # So we use asyncio.open_connection
        reader, writer = await asyncio.open_connection(host="localhost", port=port, ssl=ssl_ctx)
        with closing(writer):
            writer.write(KAFKA_GENERIC_API_VERSION_REQUEST)
            await writer.drain()
            expected_bytes = struct.unpack(">i", await reader.read(4))[0]
            received_bytes = 0
            data = []
            while received_bytes < expected_bytes:
                data.append(await reader.read(1024))
                received_bytes += len(data[-1])
        return b"".join(data)
