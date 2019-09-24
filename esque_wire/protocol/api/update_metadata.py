# FIXME autogenerated module, check for errors!
from typing import Dict, List, Optional

from dataclasses import dataclass

from esque_wire.protocol.api.base import ApiKey, RequestData, ResponseData
from esque_wire.protocol.serializers import (
    ArraySerializer,
    BaseSerializer,
    DummySerializer,
    NamedTupleSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    nullableStringSerializer,
    stringSerializer,
)


@dataclass
class PartitionStates:
    # Topic partition id
    partition: "int"  # INT32

    # The controller epoch
    controller_epoch: "int"  # INT32

    # The broker id for the leader.
    leader: "int"  # INT32

    # The leader epoch.
    leader_epoch: "int"  # INT32

    # The in sync replica ids.
    isr: List["int"]  # INT32

    # The ZK version.
    zk_version: "int"  # INT32

    # The replica ids.
    replicas: List["int"]  # INT32

    # The offline replica ids
    offline_replicas: List["int"]  # INT32


@dataclass
class TopicStates:
    # Name of topic
    topic: "str"  # STRING

    # Partition states
    partition_states: List["PartitionStates"]


@dataclass
class EndPoints:
    # The port on which the broker accepts requests.
    port: "int"  # INT32

    # The hostname of the broker.
    host: "str"  # STRING

    # The listener name.
    listener_name: "str"  # STRING

    # The security protocol type.
    security_protocol_type: "int"  # INT16


@dataclass
class LiveBrokers:
    # The broker id
    id: "int"  # INT32

    # The endpoints
    end_points: List["EndPoints"]

    # The rack
    rack: "Optional[str]"  # NULLABLE_STRING


@dataclass
class UpdateMetadataRequestData(RequestData):
    # The controller id
    controller_id: "int"  # INT32

    # The controller epoch
    controller_epoch: "int"  # INT32

    # The broker epoch
    broker_epoch: "int"  # INT64

    # Topic states
    topic_states: List["TopicStates"]

    # Live broekrs
    live_brokers: List["LiveBrokers"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.UPDATE_METADATA  # == 6


@dataclass
class UpdateMetadataResponseData(ResponseData):
    # Response error code
    error_code: "int"  # INT16

    @staticmethod
    def api_key() -> int:
        return ApiKey.UPDATE_METADATA  # == 6


partitionStatesSchemas: Dict[int, Schema] = {
    0: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer([])),
    ],
    1: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer([])),
    ],
    2: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer([])),
    ],
    3: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer([])),
    ],
    4: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
    ],
    5: [
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
    ],
}


partitionStatesSerializers: Dict[int, BaseSerializer[PartitionStates]] = {
    version: NamedTupleSerializer(PartitionStates, schema) for version, schema in partitionStatesSchemas.items()
}


endPointsSchemas: Dict[int, Schema] = {
    1: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("security_protocol_type", int16Serializer),
        ("listener_name", DummySerializer(str())),
    ],
    2: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("security_protocol_type", int16Serializer),
        ("listener_name", DummySerializer(str())),
    ],
    3: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("listener_name", stringSerializer),
        ("security_protocol_type", int16Serializer),
    ],
    4: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("listener_name", stringSerializer),
        ("security_protocol_type", int16Serializer),
    ],
    5: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("listener_name", stringSerializer),
        ("security_protocol_type", int16Serializer),
    ],
}


endPointsSerializers: Dict[int, BaseSerializer[EndPoints]] = {
    version: NamedTupleSerializer(EndPoints, schema) for version, schema in endPointsSchemas.items()
}


liveBrokersSchemas: Dict[int, Schema] = {
    0: [
        ("id", int32Serializer),
        (None, stringSerializer),
        (None, int32Serializer),
        ("end_points", DummySerializer([])),
        ("rack", DummySerializer(None)),
    ],
    1: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointsSerializers[1])),
        ("rack", DummySerializer(None)),
    ],
    2: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointsSerializers[2])),
        ("rack", nullableStringSerializer),
    ],
    3: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointsSerializers[3])),
        ("rack", nullableStringSerializer),
    ],
    4: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointsSerializers[4])),
        ("rack", nullableStringSerializer),
    ],
    5: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointsSerializers[5])),
        ("rack", nullableStringSerializer),
    ],
}


liveBrokersSerializers: Dict[int, BaseSerializer[LiveBrokers]] = {
    version: NamedTupleSerializer(LiveBrokers, schema) for version, schema in liveBrokersSchemas.items()
}


topicStatesSchemas: Dict[int, Schema] = {
    5: [("topic", stringSerializer), ("partition_states", ArraySerializer(partitionStatesSerializers[5]))]
}


topicStatesSerializers: Dict[int, BaseSerializer[TopicStates]] = {
    version: NamedTupleSerializer(TopicStates, schema) for version, schema in topicStatesSchemas.items()
}


updateMetadataRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStatesSerializers[0])),
        ("live_brokers", ArraySerializer(liveBrokersSerializers[0])),
        ("broker_epoch", DummySerializer(int())),
        ("topic_states", DummySerializer([])),
    ],
    1: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStatesSerializers[1])),
        ("live_brokers", ArraySerializer(liveBrokersSerializers[1])),
        ("broker_epoch", DummySerializer(int())),
        ("topic_states", DummySerializer([])),
    ],
    2: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStatesSerializers[2])),
        ("live_brokers", ArraySerializer(liveBrokersSerializers[2])),
        ("broker_epoch", DummySerializer(int())),
        ("topic_states", DummySerializer([])),
    ],
    3: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStatesSerializers[3])),
        ("live_brokers", ArraySerializer(liveBrokersSerializers[3])),
        ("broker_epoch", DummySerializer(int())),
        ("topic_states", DummySerializer([])),
    ],
    4: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStatesSerializers[4])),
        ("live_brokers", ArraySerializer(liveBrokersSerializers[4])),
        ("broker_epoch", DummySerializer(int())),
        ("topic_states", DummySerializer([])),
    ],
    5: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("broker_epoch", int64Serializer),
        ("topic_states", ArraySerializer(topicStatesSerializers[5])),
        ("live_brokers", ArraySerializer(liveBrokersSerializers[5])),
    ],
}


updateMetadataRequestDataSerializers: Dict[int, BaseSerializer[UpdateMetadataRequestData]] = {
    version: NamedTupleSerializer(UpdateMetadataRequestData, schema)
    for version, schema in updateMetadataRequestDataSchemas.items()
}


updateMetadataResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", int16Serializer)],
    1: [("error_code", int16Serializer)],
    2: [("error_code", int16Serializer)],
    3: [("error_code", int16Serializer)],
    4: [("error_code", int16Serializer)],
    5: [("error_code", int16Serializer)],
}


updateMetadataResponseDataSerializers: Dict[int, BaseSerializer[UpdateMetadataResponseData]] = {
    version: NamedTupleSerializer(UpdateMetadataResponseData, schema)
    for version, schema in updateMetadataResponseDataSchemas.items()
}
