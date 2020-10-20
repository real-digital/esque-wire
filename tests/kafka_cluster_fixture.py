import asyncio
import logging
import os
import re
import signal
import socket
import sys
import tarfile
import tempfile
from abc import ABC, abstractmethod
from asyncio import BaseTransport, BaseProtocol
from contextlib import closing
from pathlib import Path
from subprocess import Popen
from typing import List, Optional, NewType, Generic, TypeVar, Type, Generator, Any, Tuple, Awaitable, Coroutine
from urllib.request import urlretrieve

from jinja2 import Environment, FileSystemLoader, StrictUndefined

logger = logging.getLogger(__name__)

KAFKA_DISTRIBUTION_CACHE_DIR: Path = Path(
    os.getenv("ESQUE_WIRE_KAFKA_DISTRIBUTION_CACHE_DIR", Path(__file__).parent / "kafka_distributions")
).expanduser().absolute()

KafkaVersion = NewType("KafkaVersion", str)
KAFKA_DOWNLOAD_URL_TEMPLATE = "https://archive.apache.org/dist/kafka/{version}/kafka_2.12-{version}.tgz"
KAFKA_CONFIG_TEMPLATE_DIR = Path(__file__).parent / "kafka_config_templates"
ZK_LOG_PARSER = re.compile(r"^\[(?P<ts>[^]]+)\] (?P<level>\w+) (?P<msg>.*)", re.MULTILINE | re.DOTALL)
KAFKA_STARTUP_PATTERN = re.compile(r"\[KafkaServer id=\d+\] started \(kafka\.server\.KafkaServer\)")
_JINJA_ENV: Environment = None


def get_jinja_env() -> Environment:
    global _JINJA_ENV
    if _JINJA_ENV is None:
        _JINJA_ENV = Environment(loader=FileSystemLoader(str(KAFKA_CONFIG_TEMPLATE_DIR)), undefined=StrictUndefined)
        _JINJA_ENV.filters["split"] = split
    return _JINJA_ENV


def split(txt, char) -> str:
    return txt.split(char)


def set_ignore_sigint():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


class PortAlreadyInUse(Exception):
    pass


def get_kafka_dir(kafka_version: KafkaVersion) -> Path:
    return KAFKA_DISTRIBUTION_CACHE_DIR / f"kafka_2.12-{kafka_version}"


def netcat(hostname: str, port: int, content: str) -> str:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(5)
        sock.connect((hostname, port))
        sock.sendall(content.encode())
        sock.shutdown(socket.SHUT_WR)
        data = []
        while 1:
            data.append(sock.recv(1024))
            if data[-1] == b"":
                break
    return b"".join(data).decode()


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


def probe_port(hostname: str, port: int) -> None:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(5)
        try:
            sock.connect((hostname, port))
        except ConnectionRefusedError:
            return None
        raise PortAlreadyInUse


def assert_kafka_present(kafka_version: KafkaVersion):
    KAFKA_DISTRIBUTION_CACHE_DIR.mkdir(exist_ok=True)
    kafka_dir = get_kafka_dir(kafka_version)
    if not kafka_dir.exists():
        logger.info(f"Kafka {kafka_version} not present, downloading now")
        download_kafka(kafka_version, KAFKA_DISTRIBUTION_CACHE_DIR)
    else:
        logger.info("Kafka already present")


def download_file(url: str, local_file: Path):
    logger.info(f"Downloading from {url} to {local_file}")
    urlretrieve(url, str(local_file))


def download_kafka(kafka_version: KafkaVersion, destination: Path):
    url = KAFKA_DOWNLOAD_URL_TEMPLATE.format(version=kafka_version)

    def should_extract(member: tarfile.TarInfo) -> bool:
        pth = Path(member.name)
        if len(pth.parts) < 2:
            return False
        if pth.parts[1] == "config":
            return len(pth.parts) == 2 or pth.parts[2] == "log4j.properties"
        return pth.parts[1] in ("libs", "bin")

    with tempfile.NamedTemporaryFile(suffix=".tgz") as tmpfile:
        download_file(url, Path(tmpfile.name))
        tmpfile.file.seek(0)
        logger.info(f"Extracting kafka archive to {destination}")
        with tarfile.open(tmpfile.name) as tar:
            members = [mem for mem in tar.getmembers() if should_extract(mem)]
            tar.extractall(members=members, path=str(destination))


P = TypeVar("P", bound=Type["JavaProtocol"])


class JavaProtocol(asyncio.SubprocessProtocol):
    def __init__(self, loop: asyncio.AbstractEventLoop, logger: logging.Logger):
        super().__init__()
        self.loop = loop
        self.startup_complete = loop.create_future()
        self.disconnected = loop.create_future()
        self.exited = loop.create_future()
        self._logger = logger

    def pipe_data_received(self, fd: int, data: bytes):
        if fd == 1:  # got stdout data (bytes)
            lines = data.decode().splitlines(keepends=False)
            self.merge_lines_in_place(lines)
            for line in lines:
                self.process_log_line(line)

    def process_log_line(self, line):
        if not line.strip():
            return

        matched_line = ZK_LOG_PARSER.match(line)
        if matched_line:
            self._logger.log(level=logging.getLevelName(matched_line["level"]), msg=matched_line["msg"])
        else:
            self._logger.warning(f"Log line couldn't be parsed:\n{line}")
        self.check_startup_complete(line)

    def check_startup_complete(self, line):
        raise NotImplementedError

    @staticmethod
    def merge_lines_in_place(lines):
        i = 0
        while i < len(lines):
            while i + 1 < len(lines) and lines[i + 1][0] != "[":
                lines[i] += "\n" + lines.pop(i + 1)
            i += 1

    def connection_lost(self, exc: Optional[Exception]):
        if exc is None:
            self.disconnected.set_result(True)
            self._logger.info("Connection closed")
        else:
            if not self.startup_complete.done():
                self.startup_complete.set_exception(exc)
            self.disconnected.set_exception(exc)
            self._logger.info("Connection lost")

    def get_self(self: P) -> P:
        return self

    def process_exited(self) -> None:
        self._logger.info("Process exited")
        self.exited.set_result(True)


class Component(Generic[P], ABC):
    _process: Popen
    _proto: P
    _proto_cls: Type[P]

    def __init__(
        self,
        kafka_version: KafkaVersion = "2.5.0",
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        self._logger = logging.getLogger(f"{__name__}.{self.component_name}")

        if working_directory is None:
            self._working_directory = Path(tempfile.mkdtemp())
        else:
            self._working_directory = working_directory

        if loop is None:
            self._loop = get_loop()
        else:
            self._loop = loop

        assert_kafka_present(kafka_version)
        self._kafka_version = kafka_version

    @property
    def bin_dir(self) -> Path:
        return get_kafka_dir(self._kafka_version) / "bin"

    def start(self):
        self._loop.run_until_complete(self.async_start())

    async def async_start(self):
        while True:
            try:
                self._check_ports()
                self._render_config()
                await self._spawn_process()
                await self._wait_until_ready()
            except PortAlreadyInUse:
                self._increment_ports()
            else:
                break

    @property
    @abstractmethod
    def component_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _check_ports(self):
        raise NotImplementedError

    @abstractmethod
    def _render_config(self):
        raise NotImplementedError

    @abstractmethod
    def _subprocess_exec(self) -> Coroutine[Tuple[BaseTransport, BaseProtocol]]:
        raise NotImplementedError

    async def _spawn_process(self) -> None:
        if hasattr(self, "_process") and not self._proto.disconnected.done():
            await self._close_async()

        self._proto = self._proto_cls(self._loop, self._logger)
        transport, protocol = await self._subprocess_exec()
        self._process: Popen = transport.get_extra_info("subprocess")

    async def _wait_until_ready(self):
        await self._proto.startup_complete

    @abstractmethod
    def _increment_ports(self):
        raise NotImplementedError

    def close(self):
        if not hasattr(self, "_process") or self._proto.disconnected.done():
            return
        self._loop.run_until_complete(self._close_async())

    async def _close_async(self):
        self._logger.info("Terminating process")
        self._process.terminate()
        self._logger.info("Waiting for process to finish")

        for _ in range(20):
            if self._proto.disconnected.done():
                break
            await asyncio.sleep(0.5)
        else:
            self._logger.info("Grace period ended, sending sigkill")
            self._process.kill()

        await self._proto.disconnected
        await self._proto.exited


class ZKProtocol(JavaProtocol):
    def __init__(self, loop: asyncio.AbstractEventLoop, logger: logging.Logger):
        super().__init__(loop, logger)
        self._binding_line_seen = False

    def check_startup_complete(self, line: str):
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
        kafka_version: KafkaVersion = "2.5.0",
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        super().__init__(kafka_version, working_directory, loop)
        self._port = 2181

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
    def component_name(self) -> str:
        return "zookeeper"

    def _check_ports(self):
        probe_port("localhost", self._port)

    def _increment_ports(self):
        self._port += 1

    def _render_config(self) -> None:
        env = get_jinja_env()
        template = env.get_template("zookeeper.properties.j2")
        self.config_file.write_text(template.render(zk=self))

    def _subprocess_exec(self) -> Coroutine[Tuple[BaseTransport, BaseProtocol]]:
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
        else:
            raise TimeoutError(f"Zookeeper didn't start up in time! Last exception caught: {exc}")


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

    def with_incremented_port(self, offset: int) -> "Endpoint":
        return type(self)(self.listener_name, self.port + offset)

    @property
    def url(self) -> str:
        return f"{self.security_protocol}//localhost:{self.port}"


class PlaintextEndpoint(Endpoint):
    @property
    def security_protocol(self) -> str:
        return "PLAINTEXT"


class SaslEndpoint(Endpoint):
    @property
    def security_protocol(self) -> str:
        return "SASL_PLAINTEXT"


class KafkaProtocol(JavaProtocol):
    def __init__(self, loop: asyncio.AbstractEventLoop, logger: logging.Logger):
        super().__init__(loop, logger)

    def check_startup_complete(self, line: str):
        if self.startup_complete.done():
            return

        if "java.net.BindException" in line:
            self.startup_complete.set_exception(PortAlreadyInUse())
            return

        if KAFKA_STARTUP_PATTERN.search(line):
            self.startup_complete.set_result(True)


class KafkaInstance(Component[KafkaProtocol]):
    _proto_cls = KafkaProtocol

    def __init__(
        self,
        broker_id: int,
        zookeeper_instance: ZookeeperInstance,
        cluster_size: int = 1,
        kafka_version: KafkaVersion = "2.5.0",
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        endpoints: Optional[List[Endpoint]] = None,
        sasl_mechanisms: Optional[List[str]] = None,
    ):
        # set broker_id first so self.component_name can use it
        self.broker_id = broker_id
        super().__init__(kafka_version, working_directory, loop)

        if endpoints is None:
            endpoints = [PlaintextEndpoint()]
        self.endpoints: List[Endpoint] = [e.with_incremented_port(broker_id * len(endpoints)) for e in endpoints]

        if sasl_mechanisms is None:
            self.sasl_mechanisms = []
        else:
            self.sasl_mechanisms = sasl_mechanisms

        self._cluster_size = cluster_size
        self._zk_instance = zookeeper_instance

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

    def _subprocess_exec(self) -> Coroutine[Tuple[BaseTransport, BaseProtocol]]:
        return self._loop.subprocess_exec(
            self._proto.get_self,
            str(self.bin_dir / "kafka-server-start.sh"),
            str(self.config_file),
            env={"KAFKA_OPTS": f"-Djava.security.auth.login.config={self.sasl_config_file}"},
        )


def get_loop() -> asyncio.AbstractEventLoop:
    if os.name == "nt":
        loop = asyncio.ProactorEventLoop()  # for subprocess' pipes on Windows
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()
    return loop


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    loop = get_loop()
    # loop.set_debug(True)
    zk_instance = ZookeeperInstance(loop=loop)
    # zk_instance._logger.setLevel(logging.WARNING)
    kafka_instance = KafkaInstance(0, zk_instance, loop=loop)
    kafka_instance2 = KafkaInstance(1, zk_instance, loop=loop)

    try:
        zk_instance.start()
        logger.info(f"\n\n--> Zookeeper ready at port {zk_instance.port} <--\n")
        kafka_instance.start()
        logger.info(f"\n\n--> Kafka ready at {kafka_instance.get_endpoint_url('PLAINTEXT')} <--\n")
        kafka_instance2.start()
        logger.info(f"\n\n--> Kafka2 ready at {kafka_instance2.get_endpoint_url('PLAINTEXT')} <--\n")
        loop.run_until_complete(asyncio.sleep(3600))
        # kafka_instance.close()

        # while True:
        #     loop.run_until_complete(asyncio.sleep(1))
        #     if zk_instance._proto.terminated.done():
        #         zk_instance._proto.terminated.result()
        #         break
        #     if kafka_instance._proto.terminated.done():
        #         kafka_instance._proto.terminated.result()
        #         break
    except KeyboardInterrupt:
        pass
    finally:
        kafka_instance.close()
        kafka_instance2.close()
        zk_instance.close()
        loop.close()


if __name__ == "__main__":
    main()
