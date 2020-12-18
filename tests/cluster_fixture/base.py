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
from asyncio.protocols import BaseProtocol
from asyncio.transports import BaseTransport
from contextlib import closing
from pathlib import Path
from subprocess import Popen
from typing import Awaitable, Generic, List, NewType, Optional, Tuple, Type, TypeVar
from urllib.request import urlretrieve

from jinja2 import Environment, FileSystemLoader, StrictUndefined

# ThreadedChildWatcher was introduced in 3.8
if sys.version_info < (3, 8):
    from watcher import ThreadedChildWatcher
else:
    from asyncio import ThreadedChildWatcher

KafkaVersion = NewType("KafkaVersion", str)
P = TypeVar("P", bound="JavaProtocol")

KAFKA_DISTRIBUTION_CACHE_DIR: Path = Path(
    os.getenv("ESQUE_WIRE_KAFKA_DISTRIBUTION_CACHE_DIR", Path(__file__).parent / "kafka_distributions")
).expanduser().absolute()
KAFKA_DOWNLOAD_URL_TEMPLATE = "https://archive.apache.org/dist/kafka/{version}/kafka_2.12-{version}.tgz"
KAFKA_CONFIG_TEMPLATE_DIR = Path(__file__).parent / "kafka_config_templates"
_JINJA_ENV: Optional[Environment] = None
DEFAULT_KAFKA_VERSION: KafkaVersion = KafkaVersion("2.5.0")
JAVA_LOG_PARSER = re.compile(r"^\[(?P<ts>[^]]+)\] (?P<level>\w+) (?P<msg>.*)", re.MULTILINE | re.DOTALL)

logger = logging.getLogger(__name__)


class Component(Generic[P], ABC):
    _process: Popen
    _proto: P
    _proto_cls: Type[P]

    def __init__(
        self,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        self._logger = logging.getLogger(f"{__name__}.{self.component_name}")

        if working_directory is None:
            working_directory = Path(tempfile.mkdtemp())
        self._working_directory = working_directory
        working_directory.mkdir(parents=True, exist_ok=True)

        if loop is None:
            self._loop = get_loop()
        else:
            self._loop = loop

        assert_kafka_present(kafka_version)
        self._kafka_version = kafka_version
        self.startup_complete: Optional[asyncio.Task] = None

    @property
    def bin_dir(self) -> Path:
        return get_kafka_dir(self._kafka_version) / "bin"

    def start_async(self) -> asyncio.Task:
        self.startup_complete = self._loop.create_task(self._start_async())
        return self.startup_complete

    def start(self) -> None:
        self.start_async()
        assert self.startup_complete is not None  # to satisfy mypy
        self._loop.run_until_complete(self.startup_complete)

    async def _start_async(self) -> None:
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
    def _check_ports(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _render_config(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _subprocess_exec(self) -> Awaitable[Tuple[BaseTransport, BaseProtocol]]:
        raise NotImplementedError

    async def _spawn_process(self) -> None:
        if hasattr(self, "_process") and not self._proto.disconnected.done():
            await self.close_async()

        self._proto = self._proto_cls(self._loop, self._logger)
        transport, protocol = await self._subprocess_exec()
        self._process: Popen = transport.get_extra_info("subprocess")

    async def _wait_until_ready(self) -> None:
        await self._proto.startup_complete

    @abstractmethod
    def _increment_ports(self) -> None:
        raise NotImplementedError

    def close(self) -> None:
        if not hasattr(self, "_process") or self._proto.disconnected.done():
            return
        self._loop.run_until_complete(self.close_async())

    async def close_async(self) -> None:
        if not hasattr(self, "_proto") or self._proto.exited.done():
            return

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

    @property
    def exited(self) -> asyncio.Future:
        return self._proto.exited


class JavaProtocol(asyncio.SubprocessProtocol):
    def __init__(self, loop: asyncio.AbstractEventLoop, logger: logging.Logger):
        super().__init__()
        self.loop = loop
        self.startup_complete = loop.create_future()
        self.disconnected = loop.create_future()
        self.exited = loop.create_future()
        self._logger = logger

    def pipe_data_received(self, fd: int, data: bytes) -> None:
        if fd == 1:  # got stdout data (bytes)
            lines = data.decode().splitlines(keepends=False)
            self.merge_lines_in_place(lines)
            for line in lines:
                self.process_log_line(line)

    def process_log_line(self, line: str) -> None:
        if not line.strip():
            return

        matched_line = JAVA_LOG_PARSER.match(line)
        if matched_line:
            self._logger.log(level=logging.getLevelName(matched_line["level"]), msg=matched_line["msg"])
        else:
            self._logger.warning(f"Log line couldn't be parsed:\n{line}")
        self.check_startup_complete(line)

    def check_startup_complete(self, line: str) -> None:
        raise NotImplementedError

    @staticmethod
    def merge_lines_in_place(lines: List[str]) -> None:
        i = 0
        while i < len(lines):
            while i + 1 < len(lines) and lines[i + 1][0] != "[":
                lines[i] += "\n" + lines.pop(i + 1)
            i += 1

    def connection_lost(self, exc: Optional[Exception]) -> None:
        if not self.startup_complete.done():
            if exc is None:
                exc = RuntimeError("Connection lost before startup completion!")

        if exc is None:
            self.disconnected.set_result(True)
            self._logger.info("Connection closed")
        else:
            if not self.startup_complete.done():
                self.startup_complete.set_exception(exc)
            self.disconnected.set_exception(exc)
            self._logger.info(f"Connection lost: {exc}")

    def get_self(self: P) -> P:
        return self

    def process_exited(self) -> None:
        self._logger.info("Process exited")
        self.exited.set_result(True)


def get_loop() -> asyncio.AbstractEventLoop:
    if os.name == "nt":
        # for subprocess' pipes on Windows
        loop = asyncio.ProactorEventLoop()  # type: ignore
        asyncio.set_event_loop(loop)
    else:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    asyncio.set_child_watcher(ThreadedChildWatcher(loop))
    return loop


def set_ignore_sigint() -> None:
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def probe_port(hostname: str, port: int) -> None:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(5)
        try:
            sock.connect((hostname, port))
        except ConnectionRefusedError:
            return None
        raise PortAlreadyInUse


def get_jinja_env() -> Environment:
    global _JINJA_ENV
    if _JINJA_ENV is None:
        _JINJA_ENV = Environment(loader=FileSystemLoader(str(KAFKA_CONFIG_TEMPLATE_DIR)), undefined=StrictUndefined)
        _JINJA_ENV.filters["split"] = split
        _JINJA_ENV.filters["any"] = any
        _JINJA_ENV.filters["all"] = all
    return _JINJA_ENV


def split(txt: str, char: str) -> List[str]:
    return txt.split(char)


class PortAlreadyInUse(Exception):
    pass


def get_kafka_dir(kafka_version: KafkaVersion) -> Path:
    return KAFKA_DISTRIBUTION_CACHE_DIR / f"kafka_2.12-{kafka_version}"


def assert_kafka_present(kafka_version: KafkaVersion) -> None:
    KAFKA_DISTRIBUTION_CACHE_DIR.mkdir(exist_ok=True)
    kafka_dir = get_kafka_dir(kafka_version)
    if not kafka_dir.exists():
        logger.info(f"Kafka {kafka_version} not present, downloading now")
        download_kafka(kafka_version, KAFKA_DISTRIBUTION_CACHE_DIR)
    else:
        logger.debug("Kafka binaries already present")


def download_file(url: str, local_file: Path) -> None:
    logger.info(f"Downloading from {url} to {local_file}")
    urlretrieve(url, str(local_file))


def download_kafka(kafka_version: KafkaVersion, destination: Path) -> None:
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
        logger.info(f"Extracting kafka archive to {destination}")
        with tarfile.open(tmpfile.name) as tar:
            members = [mem for mem in tar.getmembers() if should_extract(mem)]
            tar.extractall(members=members, path=str(destination))
