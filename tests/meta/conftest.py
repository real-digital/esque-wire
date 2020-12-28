import pytest
from _pytest.fixtures import SubRequest

from tests.cluster_fixture import KafkaVersion

TESTED_KAFKA_VERSIONS = ["1.1.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0"]


@pytest.fixture(params=TESTED_KAFKA_VERSIONS, ids=[f"kafka-{v.replace('.', '_')}" for v in TESTED_KAFKA_VERSIONS])
def kafka_version(request: SubRequest) -> KafkaVersion:
    return KafkaVersion(request.param)
