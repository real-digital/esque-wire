##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.list_offsets_request import ListOffsetsRequestData, Partition, Topic

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    int32Serializer,
    int64Serializer,
    int8Serializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {
    0: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        (None, int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    1: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    2: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    3: [
        ("partition", int32Serializer),
        ("timestamp", int64Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    4: [
        ("partition", int32Serializer),
        ("current_leader_epoch", int32Serializer),
        ("timestamp", int64Serializer),
    ],
    5: [
        ("partition", int32Serializer),
        ("current_leader_epoch", int32Serializer),
        ("timestamp", int64Serializer),
    ],
}


partitionSerializers: Dict[int, DataClassSerializer[Partition]] = {
    version: DataClassSerializer(Partition, schema)
    for version, schema in partitionSchemas.items()
}


topicSchemas: Dict[int, Schema] = {
    0: [
        ("topic", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[0])),
    ],
    1: [
        ("topic", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[1])),
    ],
    2: [
        ("topic", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[2])),
    ],
    3: [
        ("topic", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[3])),
    ],
    4: [
        ("topic", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[4])),
    ],
    5: [
        ("topic", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[5])),
    ],
}


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema)
    for version, schema in topicSchemas.items()
}


listOffsetsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("replica_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[0])),
        ("isolation_level", DummySerializer(int8Serializer.default)),
    ],
    1: [
        ("replica_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[1])),
        ("isolation_level", DummySerializer(int8Serializer.default)),
    ],
    2: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[2])),
    ],
    3: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[3])),
    ],
    4: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[4])),
    ],
    5: [
        ("replica_id", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[5])),
    ],
}


listOffsetsRequestDataSerializers: Dict[
    int, DataClassSerializer[ListOffsetsRequestData]
] = {
    version: DataClassSerializer(ListOffsetsRequestData, schema)
    for version, schema in listOffsetsRequestDataSchemas.items()
}
