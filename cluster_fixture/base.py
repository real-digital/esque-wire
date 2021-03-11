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
from typing import Awaitable, Callable, List, NewType, Optional, Tuple
from urllib.request import urlretrieve

from jinja2 import Environment, FileSystemLoader, StrictUndefined

# ThreadedChildWatcher was introduced in 3.8, use custom implementation for older versions
if sys.version_info < (3, 8):
    from cluster_fixture.watcher import ThreadedChildWatcher
else:
    from asyncio import ThreadedChildWatcher

KafkaVersion = NewType("KafkaVersion", str)

KAFKA_DISTRIBUTION_CACHE_DIR: Path = Path(
    os.getenv("ESQUE_WIRE_KAFKA_DISTRIBUTION_CACHE_DIR", Path(__file__).parent / "kafka_distributions")
).expanduser().absolute()
KAFKA_DOWNLOAD_URL_TEMPLATE = "https://archive.apache.org/dist/kafka/{version}/kafka_2.12-{version}.tgz"
KAFKA_CONFIG_TEMPLATE_DIR = Path(__file__).parent / "kafka_config_templates"
_JINJA_ENV: Optional[Environment] = None
DEFAULT_KAFKA_VERSION: KafkaVersion = KafkaVersion("2.5.0")
JAVA_LOG_PARSER = re.compile(r"^\[(?P<ts>[^]]+)\] (?P<level>\w+) (?P<msg>.*)", re.MULTILINE | re.DOTALL)

logger = logging.getLogger(__name__)


class Component(ABC):
    _process: Popen
    _proto: "JavaProtocol"

    def __init__(
        self,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        """
        Base class for Kafka componentes (i.e. Zookeeper and Kafka). Provides functionality for startup, shutdown and
        free port discovery.

        :param kafka_version: The kafka version the component should use.
        :param working_directory: The working directory containing all configuration files for this component.
                                  Defaults to a temporary directory if `None`.
        :param loop: The asyncio event loop to use for communicating with this component.
                     If `None` then the running loop within the active thread will be used or a new one will be created
                     if there is no running loop.
        """
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
        """
        :return: Path to the kafka binaries/scripts for the configured kafka version.
        """
        return get_kafka_dir(self._kafka_version) / "bin"

    def start(self) -> None:
        """
        Start this component and wait until it's ready.
        """
        self.start_async()
        assert self.startup_complete is not None  # `start_async` will create it, but mypy doesn't know that
        self._loop.run_until_complete(self.startup_complete)

    def start_async(self) -> asyncio.Task:
        """
        Start this component asynchronously
        """
        self.startup_complete = self._loop.create_task(self._start_async())
        return self.startup_complete

    async def _start_async(self) -> None:
        while True:
            try:
                self._check_ports()
                self._render_config()
                await self._spawn_process()
                await self._proto.wait_until_ready()
            except PortAlreadyInUse:
                self._increment_ports()
            else:
                break

    @property
    @abstractmethod
    def component_name(self) -> str:
        """
        Return the name of this component (e.g. kafka).
        Used for logging and naming config directories.

        :return: This component's name.
        """
        raise NotImplementedError

    def _check_ports(self) -> None:
        for port in self._get_ports():
            probe_port("localhost", port)

    @abstractmethod
    def _get_ports(self) -> List[int]:
        """
        Get all ports this component is currently configured to use.

        :return: List of all ports this component is supposed to bind to.
        """
        raise NotImplementedError

    @abstractmethod
    def _render_config(self) -> None:
        """
        Render all config files for this component using the configs currently set on this object.
        """
        raise NotImplementedError

    @abstractmethod
    def _subprocess_exec(self) -> Awaitable[Tuple[BaseTransport, BaseProtocol]]:
        """
        Start the subprocess of this component.
        """
        raise NotImplementedError

    async def _spawn_process(self) -> None:
        if hasattr(self, "_process") and not self._proto.disconnected.done():
            await self.close_async()

        self._proto = JavaProtocol(self._loop, self._logger, self.probe_service)
        transport, protocol = await self._subprocess_exec()
        self._process: Popen = transport.get_extra_info("subprocess")

    @abstractmethod
    async def probe_service(self) -> bool:
        """
        Check if the service this component provides is available

        :return: `True` if it's ready, `False` otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def _increment_ports(self) -> None:
        """
        Called when one or more ports that are currently configured are not available. This method should increment
        all port numbers this component is supposed to use.
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Tell this component to stop and wait until it did.
        """
        if not hasattr(self, "_process") or self._proto.disconnected.done():
            return
        self._loop.run_until_complete(self.close_async())

    async def close_async(self) -> None:
        """
        Tell this component to stop and asynchronously wait until it did.
        Kill the process if the component doesn't shut down in time.
        """

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
        """
        Returns the :class:`asyncio.Future` that tells whether this component's process has exited or not.
        :return:
        """
        return self._proto.exited


class JavaProtocol(asyncio.SubprocessProtocol):
    STARTUP_TIMEOUT_SECS = 10
    PROBE_INTERVAL = 0.1

    def __init__(
        self, loop: asyncio.AbstractEventLoop, logger: logging.Logger, probe_routine: Callable[[], Awaitable[bool]]
    ):
        """
        Base class for Java subprocess communication.
        It's used to automatically relay logs to python's logging framework and to automatically check the process'
        status.

        :param loop: The asyncio event loop to use for communicating with this component.
                     If `None` then the running loop within the active thread will be used or a new one will be created
                     if there is no running loop.
        :param logger: The logger used to relay the subprocess logs and to log other events.
        :param probe_routine: The coroutine that's used to asynchronously check if the subprocess is ready.
        """
        super().__init__()
        self.loop = loop
        self.startup_complete = loop.create_future()
        self.disconnected = loop.create_future()
        self.exited = loop.create_future()
        self._logger = logger
        self._probe = probe_routine

    def pipe_data_received(self, fd: int, data: bytes) -> None:
        """
        Called by the protocol framework when data was received.

        :param fd: File descriptor. 1 for stdout, 2 for stderr.
        :param data: The data that was received.
        """
        if fd == 1:  # got stdout data (bytes)
            messages = data.decode().splitlines(keepends=False)
            self.merge_lines_in_place(messages)
            for msg in messages:
                self.process_log_message(msg)

    @staticmethod
    def merge_lines_in_place(lines: List[str]) -> None:
        """
        Takes a list of strings and merges all strings that do not start with '['.
        This is supposed to re-assemble log lines into blocks that belong together.

            >>> lines = [
            ...     "[some timestamp] INFO some message",
            ...     " continuation of some message",
            ...     "[some other timestamp] INFO some other message",
            ... ]
            >>> JavaProtocol.merge_lines_in_place(lines)
            >>> print(lines[0])
            [some timestamp] INFO some message
             continuation of some message
            >>> print(lines[1])
            [some other timestamp] INFO some other message

        :param lines: The lines that are supposed to be merged.
        :return: A list of merged lines.
        """
        i = 0
        while i < len(lines):
            while i + 1 < len(lines) and lines[i + 1][0] != "[":
                lines[i] += "\n" + lines.pop(i + 1)
            i += 1

    def process_log_message(self, message: str) -> None:
        """
        Process one message that was emitted from the subprocess.
        This includes parsing of timestamp, level and the message itself.

        Parsed messages will be forwarded to pythons logging framework with the same level as the original log message.
        This method also checks for Java's bind exception which are raised when a port is already in use.

        :param message: The message that shall be processed.
        """
        if not message.strip():
            return

        matched_message = JAVA_LOG_PARSER.match(message)
        if matched_message:
            self._logger.log(level=logging.getLevelName(matched_message["level"]), msg=matched_message["msg"])
        else:
            self._logger.warning(f"Log message couldn't be parsed:\n{message}")
        self._check_for_bind_exception(message)

    def _check_for_bind_exception(self, message: str) -> None:
        if self.startup_complete.done():
            return

        if "java.net.BindException" in message:
            self._logger.debug("BindException line seen.")
            self.startup_complete.set_exception(PortAlreadyInUse())

    async def wait_until_ready(self) -> None:
        """
        Asynchronously wait until the subprocess has completed startup.

        :raises TimeoutError: When the subprocess hasn't started within :attr:`JavaProtocol.STARTUP_TIMEOUT_SECS`.
        """
        exc: Optional[BaseException] = None
        for _ in range(int(self.STARTUP_TIMEOUT_SECS / self.PROBE_INTERVAL)):
            # give the service time to start
            await asyncio.sleep(self.PROBE_INTERVAL)

            # check if we got any exceptions derived from logs or lost connection
            if self.startup_complete.done():
                exc = self.startup_complete.exception()
                if exc is not None:
                    raise exc
                else:
                    # in this case startup has successfully completed
                    # and we can return right away
                    return

            try:
                success = await self._probe()
            except OSError as e:
                exc = e
                self._logger.debug(f"Probe raised exception: {e}")
                continue

            if success:
                self.startup_complete.set_result(True)
                break
        else:
            raise TimeoutError(f"Service didn't start up in time! Last exception caught: {exc}")

    def connection_lost(self, exc: Optional[Exception]) -> None:
        """
        Called by the protocol framework when the connection to the subprocess was lost.

        :param exc: Any exception that may have occurred, `None` for regular EOF.
        """
        if not self.startup_complete.done() and exc is None:
            exc = RuntimeError("Connection lost before startup completion!")

        if exc is None:
            self.disconnected.set_result(True)
            self._logger.info("Connection closed")
        else:
            if not self.startup_complete.done():
                self.startup_complete.set_exception(exc)
            self.disconnected.set_exception(exc)
            self._logger.info(f"Connection lost: {exc}")

    def get_self(self) -> "JavaProtocol":
        """
        Returns the object itself. Used as an argument to :meth:`asyncio.events.AbstractEventLoop.subprocess_exec`.
        """
        return self

    def process_exited(self) -> None:
        """
        Called by the protocol framework when the subprocess has exited.
        """
        self._logger.info("Process exited")
        self.exited.set_result(True)


def get_loop() -> asyncio.AbstractEventLoop:
    """
    Get currently running event loop or create a new one if there is no loop running yet.
    Also makes sure to use ThreadedChildWatcher so the subprocesses can be monitored by a thread that's not the main
    one.
    """
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
    asyncio.set_child_watcher(ThreadedChildWatcher())
    return loop


def set_ignore_sigint() -> None:
    """
    Used to make sure a subprocess does not immediately exit when a keyboard interrupt is sent.
    """
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def probe_port(hostname: str, port: int) -> None:
    """
    Check if the given port is free by trying to connect to it.

    :param hostname: Host to connect to.
    :param port: Port to connect to.
    :raises PortAlreadyInUse: When the connection could be established.
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(5)
        try:
            sock.connect((hostname, port))
        except ConnectionRefusedError:
            return None
        raise PortAlreadyInUse


def get_jinja_env() -> Environment:
    """
    Create templating environment that can be used to render the config files.

    :return: Jinja environment for config templating.
    """
    global _JINJA_ENV
    if _JINJA_ENV is None:
        _JINJA_ENV = Environment(loader=FileSystemLoader(str(KAFKA_CONFIG_TEMPLATE_DIR)), undefined=StrictUndefined)
        _JINJA_ENV.filters["split"] = split
        _JINJA_ENV.filters["any"] = any
        _JINJA_ENV.filters["all"] = all
    return _JINJA_ENV


def split(txt: str, char: str) -> List[str]:
    """
    Filter for jinja that allows to split strings into a list of strings.
    :param txt: The string to split.
    :param char: The character to split at.
    :return: The parts after splitting `txt` at `char`.
    """
    return txt.split(char)


class PortAlreadyInUse(Exception):
    """
    Exception that indicates that some port is already in use.
    """


def get_kafka_dir(kafka_version: KafkaVersion) -> Path:
    """
    Get the directory where the kafka distribution with the given version can be found.

    :param kafka_version: Version to look for.
    :return: Path to the directory containing the kafka distribution.
    """
    return KAFKA_DISTRIBUTION_CACHE_DIR / f"kafka_2.12-{kafka_version}"


def assert_kafka_present(kafka_version: KafkaVersion) -> None:
    """
    Make sure that the kafka distribution with the given version is present.
    Will automatically download and unpack the data if it's not.

    :param kafka_version: The version to check for presence.
    """
    KAFKA_DISTRIBUTION_CACHE_DIR.mkdir(exist_ok=True)
    kafka_dir = get_kafka_dir(kafka_version)
    if not kafka_dir.exists():
        logger.info(f"Kafka {kafka_version} not present, downloading now")
        download_kafka(kafka_version, KAFKA_DISTRIBUTION_CACHE_DIR)
    else:
        logger.debug("Kafka binaries already present")


def download_file(url: str, local_file: Path) -> None:
    """
    Download some file to local filesystem.

    :param url: The url where the file is at.
    :param local_file: The local file to download to.
    """
    logger.info(f"Downloading from {url} to {local_file}")
    urlretrieve(url, str(local_file))


def download_kafka(kafka_version: KafkaVersion, destination: Path) -> None:
    """
    Download kafka with the given version to the given directory. Unpacks only required files.

    :param kafka_version: Kafka version to download.
    :param destination: Directory to download kafka distribution to.
    """
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


async def netcat_async_string(loop: asyncio.AbstractEventLoop, hostname: str, port: int, content: str) -> str:
    """
    Run an asynchronous netcat-like request to the given host and port.

    :param loop: The asyncio event loop that's supposed to be used for the request.
    :param hostname: The host to send the request to.
    :param port: The port to send the request to.
    :param content: The request to send
    :return: The answer from the host.
    """
    response = await netcat_async_bytes(loop, hostname, port, content.encode())
    return response.decode()


async def netcat_async_bytes(loop: asyncio.AbstractEventLoop, hostname: str, port: int, content: bytes) -> bytes:
    """
    Run an asynchronous netcat-like request to the given host and port.

    :param loop: The asyncio event loop that's supposed to be used for the request.
    :param hostname: The host to send the request to.
    :param port: The port to send the request to.
    :param content: The request to send
    :return: The answer from the host.
    """

    with closing(socket.socket(type=socket.SOCK_STREAM)) as sock:
        sock.setblocking(False)
        await loop.sock_connect(sock, (hostname, port))
        await loop.sock_sendall(sock, content)
        sock.shutdown(socket.SHUT_WR)
        data = []
        while 1:
            data.append(await loop.sock_recv(sock, 1024))
            if data[-1] == b"":
                break
    return b"".join(data)
