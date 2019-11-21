from esque_wire.connection import BrokerConnection
from esque_wire.protocol.structs.api import ApiVersionsRequestData, MetadataRequestData


def test_api_versions(kafka_server):
    with BrokerConnection(kafka_server, "esque_wire_integration_test") as connection:
        data = ApiVersionsRequestData()

        response = connection.send(data)
        assert len(response.response_data.api_versions) > 0


def test_metadata(kafka_server, bootstrap_servers):
    with BrokerConnection(kafka_server, "esque_wire_integration_test") as connection:
        data = MetadataRequestData([], False, True, True)

        response = connection.send(data)
        assert len(response.response_data.brokers) == len(bootstrap_servers)
