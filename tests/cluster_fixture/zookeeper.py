import asyncio
import logging
import socket
from asyncio.protocols import BaseProtocol
from asyncio.transports import BaseTransport
from contextlib import closing
from pathlib import Path
from typing import TYPE_CHECKING, Awaitable, List, Optional, Tuple

from cluster_fixture.base import (
    DEFAULT_KAFKA_VERSION,
    Component,
    JavaProtocol,
    KafkaVersion,
    PortAlreadyInUse,
    get_jinja_env,
    probe_port,
    set_ignore_sigint,
)

if TYPE_CHECKING:
    from cluster_fixture.kafka import KafkaInstance


async def netcat_async(loop: asyncio.AbstractEventLoop, hostname: str, port: int, content: str) -> str:
    with closing(socket.socket(type=socket.SOCK_STREAM)) as sock:
        sock.setblocking(False)
        await loop.sock_connect(sock, (hostname, port))
        await loop.sock_sendall(sock, content.encode())
        sock.shutdown(socket.SHUT_WR)
        data = []
        while 1:
            data.append(await loop.sock_recv(sock, 1024))
            if data[-1] == b"":
                break
    return b"".join(data).decode()


class ZKProtocol(JavaProtocol):
    def __init__(self, loop: asyncio.AbstractEventLoop, logger: logging.Logger):
        super().__init__(loop, logger)
        self._binding_line_seen = False
        self._check_task: Optional[asyncio.Task] = None

    def check_startup_complete(self, line: str) -> None:
        if self.startup_complete.done():
            return

        if "binding to port" in line:
            self._binding_line_seen = True
            # wait for next line
            return

        if "java.net.BindException" in line:
            self.startup_complete.set_exception(PortAlreadyInUse())

        # if line after binding line is not BindException, then binding was successful
        if self._binding_line_seen:
            self.startup_complete.set_result(True)


class ZookeeperInstance(Component[ZKProtocol]):
    _proto_cls = ZKProtocol

    def __init__(
        self,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        super().__init__(kafka_version, working_directory, loop)
        self._port = 2181
        self._kafka_instances: List["KafkaInstance"] = []

    def register_broker(self, kafka_instance: "KafkaInstance") -> None:
        self._kafka_instances.append(kafka_instance)

    @property
    def data_dir(self) -> Path:
        return self._working_directory / "data"

    @property
    def config_file(self) -> Path:
        return self._working_directory / "zookeeper.properties"

    @property
    def port(self) -> int:
        return self._port

    @property
    def url(self) -> str:
        return f"localhost:{self.port}"

    @property
    def component_name(self) -> str:
        return "zookeeper"

    def _check_ports(self) -> None:
        probe_port("localhost", self._port)

    def _increment_ports(self) -> None:
        self._port += 1

    def _render_config(self) -> None:
        env = get_jinja_env()
        template = env.get_template("zookeeper.properties.j2")
        self.config_file.write_text(template.render(zk=self))

    def _subprocess_exec(self) -> Awaitable[Tuple[BaseTransport, BaseProtocol]]:
        return self._loop.subprocess_exec(
            self._proto.get_self,
            str(self.bin_dir / "zookeeper-server-start.sh"),
            str(self.config_file),
            # Make sure zookeeper doesn't shut down before kafka
            preexec_fn=set_ignore_sigint,
        )

    async def _wait_until_ready(self) -> None:
        await super()._wait_until_ready()
        exc: Optional[Exception] = None
        for _ in range(10):
            await asyncio.sleep(0.1)
            try:
                response = await netcat_async(self._loop, "localhost", self.port, "ruok")
            except OSError as e:
                exc = e
                self._logger.info(f"Netcat raised exception: {e}")
                continue
            self._logger.debug(f"Req: ruok\nResp: {response}")
            if response == "imok":
                break
            assert not self._proto.exited.done()
        else:
            raise TimeoutError(f"Zookeeper didn't start up in time! Last exception caught: {exc}")

    async def close_async(self) -> None:
        for kafka_instance in self._kafka_instances:
            self._logger.info(f"Waiting for broker {kafka_instance.broker_id} to exit")
            if hasattr(kafka_instance, "_proto"):
                await kafka_instance.exited
        await super().close_async()
