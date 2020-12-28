import pathlib
import sys
import urllib.parse
from typing import Iterable, List

import pytest

from esque_wire import BrokerConnection
from tests.cluster_fixture import KafkaVersion
from tests.cluster_fixture.cluster import Cluster

sys.path.append(str(pathlib.Path(__file__).parent.parent))


@pytest.fixture()
def cluster(kafka_version: KafkaVersion) -> Iterable[Cluster]:
    with Cluster(kafka_version=kafka_version) as kafka_cluster:
        yield kafka_cluster


@pytest.fixture
def bootstrap_servers(cluster: Cluster) -> List[str]:
    return cluster.boostrap_servers("PLAINTEXT")


@pytest.fixture
def kafka_endpoint(bootstrap_servers: List[str]) -> str:
    full_url = bootstrap_servers[0]
    parsed_url = urllib.parse.urlparse(full_url)
    return f"{parsed_url.hostname}:{parsed_url.port}"


@pytest.fixture
def connection(kafka_endpoint: str) -> Iterable[BrokerConnection]:
    with BrokerConnection(kafka_endpoint, "esque_wire_integration_test") as connection:
        yield connection
