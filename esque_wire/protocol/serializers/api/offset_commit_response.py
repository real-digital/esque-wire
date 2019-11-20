##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.offset_commit_response import (
    OffsetCommitResponseData,
    Partition,
    Topic,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {
    0: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    1: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    2: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    3: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    4: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    5: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    6: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
    7: [("partition_index", int32Serializer), ("error_code", int16Serializer)],
}


partitionSerializers: Dict[int, DataClassSerializer[Partition]] = {
    version: DataClassSerializer(Partition, schema)
    for version, schema in partitionSchemas.items()
}


topicSchemas: Dict[int, Schema] = {
    0: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[0])),
    ],
    1: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[1])),
    ],
    2: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[2])),
    ],
    3: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[3])),
    ],
    4: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[4])),
    ],
    5: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[5])),
    ],
    6: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[6])),
    ],
    7: [
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[7])),
    ],
}


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema)
    for version, schema in topicSchemas.items()
}


offsetCommitResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("topics", ArraySerializer(topicSerializers[0])),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    1: [
        ("topics", ArraySerializer(topicSerializers[1])),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    2: [
        ("topics", ArraySerializer(topicSerializers[2])),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    3: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[3])),
    ],
    4: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[4])),
    ],
    5: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[5])),
    ],
    6: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[6])),
    ],
    7: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[7])),
    ],
}


offsetCommitResponseDataSerializers: Dict[
    int, DataClassSerializer[OffsetCommitResponseData]
] = {
    version: DataClassSerializer(OffsetCommitResponseData, schema)
    for version, schema in offsetCommitResponseDataSchemas.items()
}
