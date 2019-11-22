from typing import List

import pytest

from esque_wire.connection import BrokerConnection
from esque_wire.protocol.structs.api import ApiVersionsRequestData, MetadataRequestData


@pytest.mark.integration
def test_api_versions(connection: BrokerConnection):
    data = ApiVersionsRequestData()

    response = connection.send(data)
    assert len(response.response_data.api_versions) > 0


@pytest.mark.integration
def test_metadata(connection: BrokerConnection, bootstrap_servers: List[str]):
    data = MetadataRequestData([], False, True, True)

    response = connection.send(data)
    assert len(response.response_data.brokers) == len(bootstrap_servers)
