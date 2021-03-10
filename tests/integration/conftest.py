import os
import pathlib
import re
import sys
from typing import Iterable, List

import pytest
from cluster_fixture import DEFAULT_KAFKA_VERSION, Cluster, Endpoint, KafkaVersion

from esque_wire import BrokerConnection

sys.path.append(str(pathlib.Path(__file__).parent.parent))


@pytest.fixture(scope="session")
def kafka_version() -> KafkaVersion:
    version = os.getenv("KAFKA_VERSION", DEFAULT_KAFKA_VERSION)
    assert re.match(r"\d+(.\d+){2}", version), f"Version {version!r} is not a valid semver!"
    return KafkaVersion(version)


@pytest.fixture()
def cluster(kafka_version: KafkaVersion) -> Iterable[Cluster]:
    with Cluster(kafka_version=kafka_version) as kafka_cluster:
        yield kafka_cluster


@pytest.fixture
def bootstrap_servers(cluster: Cluster) -> List[str]:
    return cluster.get_bootstrap_servers("PLAINTEXT")


@pytest.fixture
def all_endpoints(cluster: Cluster) -> List[Endpoint]:
    return cluster.get_endpoints("PLAINTEXT")


@pytest.fixture
def connection(cluster: Cluster) -> Iterable[BrokerConnection]:
    endpoint = cluster.get_endpoints(listener_name="PLAINTEXT")[0]
    with BrokerConnection(endpoint.address, "esque_wire_integration_test") as connection:
        yield connection
