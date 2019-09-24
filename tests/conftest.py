from typing import List
import sys
import pathlib
import pytest
sys.path.append(str(pathlib.Path(__file__).parent.parent))


@pytest.fixture
def bootstrap_servers() -> List[str]:
    return ["localhost:9092"]


@pytest.fixture
def kafka_server(bootstrap_servers) -> str:
    return bootstrap_servers[0]
