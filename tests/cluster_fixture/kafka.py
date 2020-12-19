import asyncio
import re
import socket
import struct
from abc import ABC, abstractmethod
from asyncio.protocols import BaseProtocol
from asyncio.transports import BaseTransport
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
from typing import Awaitable, List, Optional, Tuple

from cluster_fixture.base import DEFAULT_KAFKA_VERSION, Component, KafkaVersion, get_jinja_env, probe_port
from cluster_fixture.zookeeper import ZookeeperInstance

KAFKA_STARTUP_PATTERN = re.compile(r"\[KafkaServer id=\d+\] started \(kafka\.server\.KafkaServer\)")
KAFKA_GENERIC_API_VERSION_REQUEST = b"\x00\x00\x00\x16\x00\x12\x00\x00\x00\x00\x00\x01\x00\x0cprobe_client"


class Endpoint(ABC):
    def __init__(self, name: Optional[str] = None, port: int = 9092):
        if name is None:
            self.listener_name = self.security_protocol
        else:
            self.listener_name = name
        self.port = port

    @property
    @abstractmethod
    def security_protocol(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_secure(self) -> bool:
        raise NotImplementedError

    def with_incremented_port(self, offset: int) -> "Endpoint":
        return self.with_port(self.port + offset)

    def with_port(self, port: int) -> "Endpoint":
        return type(self)(self.listener_name, port)

    @property
    def url(self) -> str:
        return f"{self.security_protocol}//localhost:{self.port}"


class PlaintextEndpoint(Endpoint):
    @property
    def is_secure(self):
        return False

    @property
    def security_protocol(self) -> str:
        return "PLAINTEXT"


class SaslEndpoint(Endpoint):
    @property
    def is_secure(self):
        return True

    @property
    def security_protocol(self) -> str:
        return "SASL_PLAINTEXT"


@dataclass
class SaslMechanism:
    name: str


class KafkaInstance(Component):
    def __init__(
        self,
        broker_id: int,
        zookeeper_instance: ZookeeperInstance,
        cluster_size: int = 1,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        endpoints: Optional[List[Endpoint]] = None,
        sasl_mechanisms: Optional[List[SaslMechanism]] = None,
    ):
        # set broker_id first so self.component_name can use it
        self.broker_id = broker_id
        super().__init__(kafka_version, working_directory, loop)

        if endpoints is None:
            endpoints = [PlaintextEndpoint()]
        if len(endpoints) == 0:
            raise ValueError("Cannot start without endpoints!")

        self.endpoints: List[Endpoint] = [e.with_incremented_port(broker_id * len(endpoints)) for e in endpoints]

        if sasl_mechanisms is None:
            if any(endpoint.is_secure for endpoint in self.endpoints):
                self.sasl_mechanisms = [SaslMechanism("PLAIN")]
            else:
                self.sasl_mechanisms = []
        else:
            if any(endpoint.is_secure for endpoint in self.endpoints) and len(sasl_mechanisms) == 0:
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
        return f"localhost:{self._zk_instance.port}"

    @property
    def data_dir(self) -> Path:
        return self._working_directory / "data"

    @property
    def config_file(self) -> Path:
        return self._working_directory / "server.properties"

    @property
    def sasl_config_file(self) -> Path:
        return self._working_directory / "sasl_jaas.conf"

    def get_endpoint_url(self, listener_name: str) -> str:
        for e in self.endpoints:
            if e.listener_name == listener_name:
                break
        else:
            raise KeyError(listener_name)
        return e.url

    def _check_ports(self) -> None:
        for endpoint in self.endpoints:
            probe_port("localhost", endpoint.port)

    def _increment_ports(self) -> None:
        for endpoint in self.endpoints:
            endpoint.port += self._cluster_size

    def _render_config(self) -> None:
        env = get_jinja_env()
        server_conf_template = env.get_template("server.properties.j2")
        sasl_conf_template = env.get_template("sasl_jaas.conf.j2")
        self.config_file.write_text(server_conf_template.render(broker=self))
        self.sasl_config_file.write_text(sasl_conf_template.render(broker=self))

    def _subprocess_exec(self) -> Awaitable[Tuple[BaseTransport, BaseProtocol]]:
        return self._loop.subprocess_exec(
            self._proto.get_self,
            str(self.bin_dir / "kafka-server-start.sh"),
            str(self.config_file),
            env={"KAFKA_OPTS": f"-Djava.security.auth.login.config={self.sasl_config_file}"},
        )

    async def probe_service(self) -> bool:
        port = self.endpoints[0].port

        with closing(socket.socket(type=socket.SOCK_STREAM)) as sock:
            sock.setblocking(False)
            await self._loop.sock_connect(sock, ("localhost", port))
            await self._loop.sock_sendall(sock, KAFKA_GENERIC_API_VERSION_REQUEST)
            datalen = struct.unpack(">i", await self._loop.sock_recv(sock, 4))[0]
            received = 0
            data = []
            while received < datalen:
                data.append(await self._loop.sock_recv(sock, 1024))
                received += len(data[-1])
            sock.shutdown(socket.SHUT_WR)
        response = b"".join(data)
        self._logger.debug(f"Requested api versions\nResponse length: {len(response)}")
        return len(response) > 0
