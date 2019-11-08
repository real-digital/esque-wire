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
class Partitions:
    # The partition index.
    partition_index: "int"  # INT32

    # The message offset to be committed.
    committed_offset: "int"  # INT64

    # The leader epoch of this partition.
    committed_leader_epoch: "int"  # INT32

    # Any associated metadata the client wants to keep.
    committed_metadata: "Optional[str]"  # NULLABLE_STRING


@dataclass
class Topics:
    # The topic name.
    name: "str"  # STRING

    # Each partition to commit offsets for.
    partitions: List["Partitions"]


@dataclass
class OffsetCommitRequestData(RequestData):
    # The unique group identifier.
    group_id: "str"  # STRING

    # The generation of the group.
    generation_id: "int"  # INT32

    # The member ID assigned by the group coordinator.
    member_id: "str"  # STRING

    # The unique identifier of the consumer instance provided by end user.
    group_instance_id: "Optional[str]"  # NULLABLE_STRING

    # The topics to commit offsets for.
    topics: List["Topics"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.OFFSET_COMMIT  # == 8


@dataclass
class Partitions:
    # The partition index.
    partition_index: "int"  # INT32

    # The error code, or 0 if there was no error.
    error_code: "int"  # INT16


@dataclass
class Topics:
    # The topic name.
    name: "str"  # STRING

    # The responses for each partition in the topic.
    partitions: List["Partitions"]


@dataclass
class OffsetCommitResponseData(ResponseData):
    # The duration in milliseconds for which the request was throttled due to a quota violation, or zero
    # if the request did not violate any quota.
    throttle_time_ms: "int"  # INT32

    # The responses for each topic.
    topics: List["Topics"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.OFFSET_COMMIT  # == 8


partitionsSchemas: Dict[int, Schema] = {
    0: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_metadata", nullableStringSerializer),
        ("committed_leader_epoch", DummySerializer(int())),
    ],
    1: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        (None, int64Serializer),
        ("committed_metadata", nullableStringSerializer),
        ("committed_leader_epoch", DummySerializer(int())),
    ],
    2: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_metadata", nullableStringSerializer),
        ("committed_leader_epoch", DummySerializer(int())),
    ],
    3: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_metadata", nullableStringSerializer),
        ("committed_leader_epoch", DummySerializer(int())),
    ],
    4: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_metadata", nullableStringSerializer),
        ("committed_leader_epoch", DummySerializer(int())),
    ],
    5: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_metadata", nullableStringSerializer),
        ("committed_leader_epoch", DummySerializer(int())),
    ],
    6: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_leader_epoch", int32Serializer),
        ("committed_metadata", nullableStringSerializer),
    ],
    7: [
        ("partition_index", int32Serializer),
        ("committed_offset", int64Serializer),
        ("committed_leader_epoch", int32Serializer),
        ("committed_metadata", nullableStringSerializer),
    ],
}


partitionsSerializers: Dict[int, BaseSerializer[Partitions]] = {
    version: NamedTupleSerializer(Partitions, schema) for version, schema in partitionsSchemas.items()
}


topicsSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[0]))],
    1: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[1]))],
    2: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[2]))],
    3: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[3]))],
    4: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[4]))],
    5: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[5]))],
    6: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[6]))],
    7: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[7]))],
}


topicsSerializers: Dict[int, BaseSerializer[Topics]] = {
    version: NamedTupleSerializer(Topics, schema) for version, schema in topicsSchemas.items()
}


offsetCommitRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("group_id", stringSerializer),
        ("topics", ArraySerializer(topicsSerializers[0])),
        ("generation_id", DummySerializer(int())),
        ("member_id", DummySerializer(str())),
        ("group_instance_id", DummySerializer(None)),
    ],
    1: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("topics", ArraySerializer(topicsSerializers[1])),
        ("group_instance_id", DummySerializer(None)),
    ],
    2: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        (None, int64Serializer),
        ("topics", ArraySerializer(topicsSerializers[2])),
        ("group_instance_id", DummySerializer(None)),
    ],
    3: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        (None, int64Serializer),
        ("topics", ArraySerializer(topicsSerializers[3])),
        ("group_instance_id", DummySerializer(None)),
    ],
    4: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        (None, int64Serializer),
        ("topics", ArraySerializer(topicsSerializers[4])),
        ("group_instance_id", DummySerializer(None)),
    ],
    5: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("topics", ArraySerializer(topicsSerializers[5])),
        ("group_instance_id", DummySerializer(None)),
    ],
    6: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("topics", ArraySerializer(topicsSerializers[6])),
        ("group_instance_id", DummySerializer(None)),
    ],
    7: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("group_instance_id", nullableStringSerializer),
        ("topics", ArraySerializer(topicsSerializers[7])),
    ],
}


offsetCommitRequestDataSerializers: Dict[int, BaseSerializer[OffsetCommitRequestData]] = {
    version: NamedTupleSerializer(OffsetCommitRequestData, schema)
    for version, schema in offsetCommitRequestDataSchemas.items()
}


partitionsSchemas: Dict[int, Schema] = {
    0: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    1: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    2: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    3: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    4: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    5: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    6: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    7: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
}


partitionsSerializers: Dict[int, BaseSerializer[Partitions]] = {
    version: NamedTupleSerializer(Partitions, schema) for version, schema in partitionsSchemas.items()
}


topicsSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[0]))],
    1: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[1]))],
    2: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[2]))],
    3: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[3]))],
    4: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[4]))],
    5: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[5]))],
    6: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[6]))],
    7: [("name", stringSerializer), ("partitions", ArraySerializer(partitionsSerializers[7]))],
}


topicsSerializers: Dict[int, BaseSerializer[Topics]] = {
    version: NamedTupleSerializer(Topics, schema) for version, schema in topicsSchemas.items()
}


offsetCommitResponseDataSchemas: Dict[int, Schema] = {
    0: [("topics", ArraySerializer(topicsSerializers[0])), ("throttle_time_ms", DummySerializer(int()))],
    1: [("topics", ArraySerializer(topicsSerializers[1])), ("throttle_time_ms", DummySerializer(int()))],
    2: [("topics", ArraySerializer(topicsSerializers[2])), ("throttle_time_ms", DummySerializer(int()))],
    3: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[3]))],
    4: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[4]))],
    5: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[5]))],
    6: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[6]))],
    7: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicsSerializers[7]))],
}


offsetCommitResponseDataSerializers: Dict[int, BaseSerializer[OffsetCommitResponseData]] = {
    version: NamedTupleSerializer(OffsetCommitResponseData, schema)
    for version, schema in offsetCommitResponseDataSchemas.items()
}