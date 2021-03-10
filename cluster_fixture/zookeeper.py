import asyncio
import logging
from asyncio.protocols import BaseProtocol
from asyncio.transports import BaseTransport
from pathlib import Path
from typing import TYPE_CHECKING, Awaitable, List, Optional, Tuple

from cluster_fixture.base import (
    DEFAULT_KAFKA_VERSION,
    Component,
    KafkaVersion,
    get_jinja_env,
    netcat_async_string,
    set_ignore_sigint,
)

if TYPE_CHECKING:
    from cluster_fixture.kafka import KafkaInstance

logger = logging.getLogger(__name__)


class ZookeeperInstance(Component):
    def __init__(
        self,
        kafka_version: KafkaVersion = DEFAULT_KAFKA_VERSION,
        working_directory: Optional[Path] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
    ):
        """
        The zookeeper component of a Kafka cluster. For more information see :class:`Component`.

        :param kafka_version: The kafka version the component should use.
        :param working_directory: The working directory containing all configuration files for this broker.
                                  Defaults to a temporary directory if `None`.
        :param loop: The asyncio event loop to use for communicating with the broker.
                     If `None` then the running loop within the active thread will be used or a new one will be created
                     if there is no running loop.
        """
        super().__init__(kafka_version, working_directory, loop)
        self._port = 2181
        self._kafka_instances: List["KafkaInstance"] = []

    def register_broker(self, kafka_instance: "KafkaInstance") -> None:
        """
        Register a broker that is connected to this zookeeper instance. Required to make sure the zookeeper instance
        doesn't shut down before the broker does. This is necessary since the broker is not able to shutdown gracefully
        when zookeeper connection is lost.

        :param kafka_instance: The kafka instance to add.
        """
        self._kafka_instances.append(kafka_instance)

    @property
    def data_dir(self) -> Path:
        """
        Used within the config template to determine the directory where the key-value data is stored.
        """
        return self._working_directory / "data"

    @property
    def config_file(self) -> Path:
        """
        Path to this zookeeper node's main configuration file.
        """
        return self._working_directory / "zookeeper.properties"

    @property
    def port(self) -> int:
        """
        Port this zookeeper node is supposed to bind to.
        """
        return self._port

    @property
    def url(self) -> str:
        """
        Url where this zookeeper node is reachable at. It's in the form `host:port`, e.g `"localhost:8081"`.
        """
        return f"localhost:{self.port}"

    @property
    def component_name(self) -> str:
        return "zookeeper"

    def _get_ports(self) -> List[int]:
        return [self._port]

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

    async def close_async(self) -> None:
        for kafka_instance in self._kafka_instances:
            self._logger.info(f"Waiting for broker {kafka_instance.broker_id} to exit")
            if hasattr(kafka_instance, "_proto"):
                await kafka_instance.exited
        await super().close_async()

    async def probe_service(self) -> bool:
        response = await netcat_async_string(self._loop, "localhost", self.port, "ruok")
        self._logger.debug(f"Req: ruok\nResp: {response}")
        return response == "imok"
