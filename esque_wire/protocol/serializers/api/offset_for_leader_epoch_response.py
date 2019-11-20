##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.offset_for_leader_epoch_response import OffsetForLeaderEpochResponseData, Partition, Topic
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)

partitionSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("partition", int32Serializer),
        ("end_offset", int64Serializer),
        ("leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("partition", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("end_offset", int64Serializer),
    ],
    2: [
        ("error_code", errorCodeSerializer),
        ("partition", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("end_offset", int64Serializer),
    ],
    3: [
        ("error_code", errorCodeSerializer),
        ("partition", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("end_offset", int64Serializer),
    ],
}


partitionSerializers: Dict[int, ClassSerializer[Partition]] = {
    version: ClassSerializer(Partition, schema) for version, schema in partitionSchemas.items()
}

partitionSerializers[-1] = partitionSerializers[3]


topicSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[0]))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[1]))],
    2: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[2]))],
    3: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[3]))],
}


topicSerializers: Dict[int, ClassSerializer[Topic]] = {
    version: ClassSerializer(Topic, schema) for version, schema in topicSchemas.items()
}

topicSerializers[-1] = topicSerializers[3]


offsetForLeaderEpochResponseDataSchemas: Dict[int, Schema] = {
    0: [("topics", ArraySerializer(topicSerializers[0])), ("throttle_time_ms", DummySerializer(0))],
    1: [("topics", ArraySerializer(topicSerializers[1])), ("throttle_time_ms", DummySerializer(0))],
    2: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicSerializers[2]))],
    3: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicSerializers[3]))],
}


offsetForLeaderEpochResponseDataSerializers: Dict[int, ClassSerializer[OffsetForLeaderEpochResponseData]] = {
    version: ClassSerializer(OffsetForLeaderEpochResponseData, schema)
    for version, schema in offsetForLeaderEpochResponseDataSchemas.items()
}

offsetForLeaderEpochResponseDataSerializers[-1] = offsetForLeaderEpochResponseDataSerializers[3]
