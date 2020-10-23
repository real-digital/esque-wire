import pathlib
import sys
from typing import Iterable, List

import pytest

from esque_wire import BrokerConnection

sys.path.append(str(pathlib.Path(__file__).parent.parent))


@pytest.fixture
def bootstrap_servers() -> List[str]:
    return ["localhost:9092"]


@pytest.fixture
def kafka_server(bootstrap_servers: List[str]) -> str:
    return bootstrap_servers[0]


@pytest.fixture
def connection(kafka_server: str) -> Iterable[BrokerConnection]:
    with BrokerConnection(kafka_server, "esque_wire_integration_test") as connection:
        yield connection
