from typing import List

import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest
from _pytest.nodes import Item

SUPPORTED_KAFKA_VERSIONS = ["1.1.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0"]


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


@pytest.fixture(params=SUPPORTED_KAFKA_VERSIONS, ids=[f"kafka-{v.replace('.','_')}" for v in SUPPORTED_KAFKA_VERSIONS])
def kafka_version(request: SubRequest) -> str:
    return request.param
