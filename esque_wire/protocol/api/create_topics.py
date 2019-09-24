from typing import Dict, List, Optional

from dataclasses import dataclass

from esque_wire.protocol.api.base import ApiKey, RequestData, ResponseData
from esque_wire.protocol.serializers import (
    ArraySerializer,
    BaseSerializer,
    DummySerializer,
    NamedTupleSerializer,
    Schema,
    booleanSerializer,
    int16Serializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


@dataclass
class Assignment:
    # The partition index.
    partition_index: "int"  # INT32

    # The brokers to place the partition on.
    broker_ids: List["int"]  # INT32


@dataclass
class Config:
    # The configuration name.
    name: "str"  # STRING

    # The configuration value.
    value: "Optional[str]"  # NULLABLE_STRING


@dataclass
class Topic:
    # The configuration name.
    name: "str"  # STRING

    # The number of partitions to create in the topic, or -1 if we are specifying a manual partition
    # assignment.
    num_partitions: "int"  # INT32

    # The number of replicas to create for each partition in the topic, or -1 if we are specifying a
    # manual partition assignment.
    replication_factor: "int"  # INT16

    # The manual partition assignment, or the empty array if we are using automatic assignment.
    assignments: List["Assignment"]

    # The custom topic configurations to set.
    configs: List["Config"]


@dataclass
class CreateTopicsRequestData(RequestData):
    # The topics to create.
    topics: List["Topic"]

    # How long to wait in milliseconds before timing out the request.
    timeout_ms: "int"  # INT32

    # If true, check that the topics can be created as specified, but don't create anything.
    validate_only: "bool"  # BOOLEAN

    @staticmethod
    def api_key() -> int:
        return ApiKey.CREATE_TOPICS  # == 19


@dataclass
class TopicCreationResult:
    # The topic name.
    name: "str"  # STRING

    # The error code, or 0 if there was no error.
    error_code: "int"  # INT16

    # The error message, or null if there was no error.
    error_message: "Optional[str]"  # NULLABLE_STRING


@dataclass
class CreateTopicsResponseData(ResponseData):
    # The duration in milliseconds for which the request was throttled due to a quota violation, or zero
    # if the request did not violate any quota.
    throttle_time_ms: "int"  # INT32

    # Results for each topic we tried to create.
    topics: List["TopicCreationResult"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.CREATE_TOPICS  # == 19


assignmentSchemas: Dict[int, Schema] = {
    0: [("partition_index", int32Serializer), ("broker_ids", ArraySerializer(int32Serializer))],
    1: [("partition_index", int32Serializer), ("broker_ids", ArraySerializer(int32Serializer))],
    2: [("partition_index", int32Serializer), ("broker_ids", ArraySerializer(int32Serializer))],
    3: [("partition_index", int32Serializer), ("broker_ids", ArraySerializer(int32Serializer))],
}


assignmentSerializers: Dict[int, BaseSerializer[Assignment]] = {
    version: NamedTupleSerializer(Assignment, schema) for version, schema in assignmentSchemas.items()
}


configSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("value", nullableStringSerializer)],
    1: [("name", stringSerializer), ("value", nullableStringSerializer)],
    2: [("name", stringSerializer), ("value", nullableStringSerializer)],
    3: [("name", stringSerializer), ("value", nullableStringSerializer)],
}


configSerializers: Dict[int, BaseSerializer[Config]] = {
    version: NamedTupleSerializer(Config, schema) for version, schema in configSchemas.items()
}


topicSchemas: Dict[int, Schema] = {
    0: [
        ("name", stringSerializer),
        ("num_partitions", int32Serializer),
        ("replication_factor", int16Serializer),
        ("assignments", ArraySerializer(assignmentSerializers[0])),
        ("configs", ArraySerializer(configSerializers[0])),
    ],
    1: [
        ("name", stringSerializer),
        ("num_partitions", int32Serializer),
        ("replication_factor", int16Serializer),
        ("assignments", ArraySerializer(assignmentSerializers[1])),
        ("configs", ArraySerializer(configSerializers[1])),
    ],
    2: [
        ("name", stringSerializer),
        ("num_partitions", int32Serializer),
        ("replication_factor", int16Serializer),
        ("assignments", ArraySerializer(assignmentSerializers[2])),
        ("configs", ArraySerializer(configSerializers[2])),
    ],
    3: [
        ("name", stringSerializer),
        ("num_partitions", int32Serializer),
        ("replication_factor", int16Serializer),
        ("assignments", ArraySerializer(assignmentSerializers[3])),
        ("configs", ArraySerializer(configSerializers[3])),
    ],
}


topicSerializers: Dict[int, BaseSerializer[Topic]] = {
    version: NamedTupleSerializer(Topic, schema) for version, schema in topicSchemas.items()
}


createTopicsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("topics", ArraySerializer(topicSerializers[0])),
        ("timeout_ms", int32Serializer),
        ("validate_only", DummySerializer(bool())),
    ],
    1: [
        ("topics", ArraySerializer(topicSerializers[1])),
        ("timeout_ms", int32Serializer),
        ("validate_only", booleanSerializer),
    ],
    2: [
        ("topics", ArraySerializer(topicSerializers[2])),
        ("timeout_ms", int32Serializer),
        ("validate_only", booleanSerializer),
    ],
    3: [
        ("topics", ArraySerializer(topicSerializers[3])),
        ("timeout_ms", int32Serializer),
        ("validate_only", booleanSerializer),
    ],
}


createTopicsRequestDataSerializers: Dict[int, BaseSerializer[CreateTopicsRequestData]] = {
    version: NamedTupleSerializer(CreateTopicsRequestData, schema)
    for version, schema in createTopicsRequestDataSchemas.items()
}


topicCreationResultSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("error_code", int16Serializer), ("error_message", DummySerializer(None))],
    1: [("name", stringSerializer), ("error_code", int16Serializer), ("error_message", nullableStringSerializer)],
    2: [("name", stringSerializer), ("error_code", int16Serializer), ("error_message", nullableStringSerializer)],
    3: [("name", stringSerializer), ("error_code", int16Serializer), ("error_message", nullableStringSerializer)],
}


topicCreationResultSerializers: Dict[int, BaseSerializer[TopicCreationResult]] = {
    version: NamedTupleSerializer(TopicCreationResult, schema) for version, schema in topicSchemas.items()
}


createTopicsResponseDataSchemas: Dict[int, Schema] = {
    0: [("topics", ArraySerializer(topicCreationResultSerializers[0])), ("throttle_time_ms", DummySerializer(int()))],
    1: [("topics", ArraySerializer(topicCreationResultSerializers[1])), ("throttle_time_ms", DummySerializer(int()))],
    2: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicCreationResultSerializers[2]))],
    3: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicCreationResultSerializers[3]))],
}


createTopicsResponseDataSerializers: Dict[int, BaseSerializer[CreateTopicsResponseData]] = {
    version: NamedTupleSerializer(CreateTopicsResponseData, schema)
    for version, schema in createTopicsResponseDataSchemas.items()
}
