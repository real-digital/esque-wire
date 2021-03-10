from typing import List

from esque_wire.connection import BrokerConnection
from esque_wire.protocol.structs.api import ApiVersionsRequestData, MetadataRequestData


def test_api_versions(connection: BrokerConnection) -> None:
    data = ApiVersionsRequestData()

    response = connection.send(data)
    assert len(response.response_data.api_versions) > 0


def test_metadata(connection: BrokerConnection, bootstrap_servers: List[str]) -> None:
    data = MetadataRequestData([], False, True, True)

    response = connection.send(data)
    assert len(response.response_data.brokers) == len(bootstrap_servers)
