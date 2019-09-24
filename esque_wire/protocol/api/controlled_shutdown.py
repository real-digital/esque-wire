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
    stringSerializer,
)


@dataclass
class ControlledShutdownRequestData(RequestData):
    # The id of the broker for which controlled shutdown has been requested.
    broker_id: "int"  # INT32

    # The broker epoch.
    broker_epoch: "int"  # INT64

    @staticmethod
    def api_key() -> int:
        return ApiKey.CONTROLLED_SHUTDOWN  # == 7


@dataclass
class RemainingPartitions:
    # The name of the topic.
    topic_name: "str"  # STRING

    # The index of the partition.
    partition_index: "int"  # INT32


@dataclass
class ControlledShutdownResponseData(ResponseData):
    # The top-level error code.
    error_code: "int"  # INT16

    # The partitions that the broker still leads.
    remaining_partitions: List["RemainingPartitions"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.CONTROLLED_SHUTDOWN  # == 7


controlledShutdownRequestDataSchemas: Dict[int, Schema] = {
    0: [("broker_id", int32Serializer), ("broker_epoch", DummySerializer(int()))],
    1: [("broker_id", int32Serializer), ("broker_epoch", DummySerializer(int()))],
    2: [("broker_id", int32Serializer), ("broker_epoch", int64Serializer)],
}


controlledShutdownRequestDataSerializers: Dict[int, BaseSerializer[ControlledShutdownRequestData]] = {
    version: NamedTupleSerializer(ControlledShutdownRequestData, schema)
    for version, schema in controlledShutdownRequestDataSchemas.items()
}


remainingPartitionsSchemas: Dict[int, Schema] = {
    0: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
    1: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
    2: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
}


remainingPartitionsSerializers: Dict[int, BaseSerializer[RemainingPartitions]] = {
    version: NamedTupleSerializer(RemainingPartitions, schema)
    for version, schema in remainingPartitionsSchemas.items()
}


controlledShutdownResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", int16Serializer), ("remaining_partitions", ArraySerializer(remainingPartitionsSerializers[0]))],
    1: [("error_code", int16Serializer), ("remaining_partitions", ArraySerializer(remainingPartitionsSerializers[1]))],
    2: [("error_code", int16Serializer), ("remaining_partitions", ArraySerializer(remainingPartitionsSerializers[2]))],
}


controlledShutdownResponseDataSerializers: Dict[int, BaseSerializer[ControlledShutdownResponseData]] = {
    version: NamedTupleSerializer(ControlledShutdownResponseData, schema)
    for version, schema in controlledShutdownResponseDataSchemas.items()
}
