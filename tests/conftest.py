import os
import re
from typing import List

import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item

from tests.cluster_fixture import DEFAULT_KAFKA_VERSION, KafkaVersion


def pytest_addoption(parser: Parser) -> None:
    parser.addoption("--integration", action="store_true", default=False, help="run integration tests")


def pytest_collection_modifyitems(config: Config, items: List[Item]) -> None:
    if config.getoption("--integration"):
        # --integration given in cli: do not skip integration tests
        return
    integration = pytest.mark.skip(reason="need --integration option to run")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(integration)


@pytest.fixture(scope="session")
def kafka_version() -> KafkaVersion:
    version = os.getenv("KAFKA_VERSION", DEFAULT_KAFKA_VERSION)
    assert re.match(r"\d+(.\d+){2}", version), f"Version {version!r} is not a valid semver!"
    return KafkaVersion(version)
