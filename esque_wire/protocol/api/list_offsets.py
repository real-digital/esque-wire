# FIXME autogenerated module, check for errors!
from typing import Dict, List

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
    int8Serializer,
    stringSerializer,
)


@dataclass
class Partitions:
    # Topic partition id
    partition: "int"  # INT32

    # The current leader epoch, if provided, is used to fence consumers/replicas with old metadata. If the
    # epoch provided by the client is larger than the current epoch known to the broker, then the
    # UNKNOWN_LEADER_EPOCH error code will be returned. If the provided epoch is smaller, then the
    # FENCED_LEADER_EPOCH error code will be returned.
    current_leader_epoch: "int"  # INT32

    # The target timestamp for the partition.
    timestamp: "int"  # INT64


@dataclass
class Topics:
    # Name of topic
    topic: "str"  # STRING

    # Partitions to list offsets.
    partitions: List["Partitions"]


@dataclass
class ListOffsetsRequestData(RequestData):
    # Broker id of the follower. For normal consumers, use -1.
    replica_id: "int"  # INT32

    # This setting controls the visibility of transactional records. Using READ_UNCOMMITTED
    # (isolation_level = 0) makes all records visible. With READ_COMMITTED (isolation_level = 1), non-
    # transactional and COMMITTED transactional records are visible. To be more concrete, READ_COMMITTED
    # returns all data from offsets smaller than the current LSO (last stable offset), and enables the
    # inclusion of the list of aborted transactions in the result, which allows consumers to discard
    # ABORTED transactional records
    isolation_level: "int"  # INT8

    # Topics to list offsets.
    topics: List["Topics"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.LIST_OFFSETS  # == 2


@dataclass
class PartitionResponses:
    # Topic partition id
    partition: "int"  # INT32

    # Response error code
    error_code: "int"  # INT16

    # The timestamp associated with the returned offset
    timestamp: "int"  # INT64

    # The offset found
    offset: "int"  # INT64

    # The leader epoch
    leader_epoch: "int"  # INT32


@dataclass
class Responses:
    # Name of topic
    topic: "str"  # STRING

    # The listed offsets by partition
    partition_responses: List["PartitionResponses"]


@dataclass
class ListOffsetsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    # The listed offsets by topic
    responses: List["Responses"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.LIST_OFFSETS  # == 2


partitionsSchemas: Dict[int, Schema] = {
    0: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        (None, int32Serializer),
        ("current_leader_epoch", DummySerializer(int())),
    ],
    1: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        ("current_leader_epoch", DummySerializer(int())),
    ],
    2: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        ("current_leader_epoch", DummySerializer(int())),
    ],
    3: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        ("current_leader_epoch", DummySerializer(int())),
    ],
    4: [("partition", int32Serializer), ("current_leader_epoch", int32Serializer), ("timestamp", int64Serializer)],
    5: [("partition", int32Serializer), ("current_leader_epoch", int32Serializer), ("timestamp", int64Serializer)],
}


partitionsSerializers: Dict[int, BaseSerializer[Partitions]] = {
    version: NamedTupleSerializer(Partitions, schema) for version, schema in partitionsSchemas.items()
}


topicsSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[0]))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[1]))],
    2: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[2]))],
    3: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[3]))],
    4: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[4]))],
    5: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[5]))],
}


topicsSerializers: Dict[int, BaseSerializer[Topics]] = {
    version: NamedTupleSerializer(Topics, schema) for version, schema in topicsSchemas.items()
}


listOffsetsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("replica_id", int32Serializer),
        ("topics", ArraySerializer(topicsSerializers[0])),
        ("isolation_level", DummySerializer(int())),
    ],
    1: [
        ("replica_id", int32Serializer),
        ("topics", ArraySerializer(topicsSerializers[1])),
        ("isolation_level", DummySerializer(int())),
    ],
    2: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicsSerializers[2])),
    ],
    3: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicsSerializers[3])),
    ],
    4: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicsSerializers[4])),
    ],
    5: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicsSerializers[5])),
    ],
}


listOffsetsRequestDataSerializers: Dict[int, BaseSerializer[ListOffsetsRequestData]] = {
    version: NamedTupleSerializer(ListOffsetsRequestData, schema)
    for version, schema in listOffsetsRequestDataSchemas.items()
}


partitionResponsesSchemas: Dict[int, Schema] = {
    0: [
        ("partition", int32Serializer),
        ("error_code", int16Serializer),
        (None, ArraySerializer(int64Serializer)),
        ("timestamp", DummySerializer(int())),
        ("offset", DummySerializer(int())),
        ("leader_epoch", DummySerializer(int())),
    ],
    1: [
        ("partition", int32Serializer),
        ("error_code", int16Serializer),
        ("timestamp", int64Serializer),
        ("offset", int64Serializer),
        ("leader_epoch", DummySerializer(int())),
    ],
    2: [
        ("partition", int32Serializer),
        ("error_code", int16Serializer),
        ("timestamp", int64Serializer),
        ("offset", int64Serializer),
        ("leader_epoch", DummySerializer(int())),
    ],
    3: [
        ("partition", int32Serializer),
        ("error_code", int16Serializer),
        ("timestamp", int64Serializer),
        ("offset", int64Serializer),
        ("leader_epoch", DummySerializer(int())),
    ],
    4: [
        ("partition", int32Serializer),
        ("error_code", int16Serializer),
        ("timestamp", int64Serializer),
        ("offset", int64Serializer),
        ("leader_epoch", int32Serializer),
    ],
    5: [
        ("partition", int32Serializer),
        ("error_code", int16Serializer),
        ("timestamp", int64Serializer),
        ("offset", int64Serializer),
        ("leader_epoch", int32Serializer),
    ],
}


partitionResponsesSerializers: Dict[int, BaseSerializer[PartitionResponses]] = {
    version: NamedTupleSerializer(PartitionResponses, schema) for version, schema in partitionResponsesSchemas.items()
}


responsesSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partition_responses", ArraySerializer(partitionResponsesSerializers[0]))],
    1: [("topic", stringSerializer), ("partition_responses", ArraySerializer(partitionResponsesSerializers[1]))],
    2: [("topic", stringSerializer), ("partition_responses", ArraySerializer(partitionResponsesSerializers[2]))],
    3: [("topic", stringSerializer), ("partition_responses", ArraySerializer(partitionResponsesSerializers[3]))],
    4: [("topic", stringSerializer), ("partition_responses", ArraySerializer(partitionResponsesSerializers[4]))],
    5: [("topic", stringSerializer), ("partition_responses", ArraySerializer(partitionResponsesSerializers[5]))],
}


responsesSerializers: Dict[int, BaseSerializer[Responses]] = {
    version: NamedTupleSerializer(Responses, schema) for version, schema in responsesSchemas.items()
}


listOffsetsResponseDataSchemas: Dict[int, Schema] = {
    0: [("responses", ArraySerializer(responsesSerializers[0])), ("throttle_time_ms", DummySerializer(int()))],
    1: [("responses", ArraySerializer(responsesSerializers[1])), ("throttle_time_ms", DummySerializer(int()))],
    2: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responsesSerializers[2]))],
    3: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responsesSerializers[3]))],
    4: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responsesSerializers[4]))],
    5: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responsesSerializers[5]))],
}


listOffsetsResponseDataSerializers: Dict[int, BaseSerializer[ListOffsetsResponseData]] = {
    version: NamedTupleSerializer(ListOffsetsResponseData, schema)
    for version, schema in listOffsetsResponseDataSchemas.items()
}
