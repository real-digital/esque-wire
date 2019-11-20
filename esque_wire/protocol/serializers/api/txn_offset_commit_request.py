##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.txn_offset_commit_request import (
    Partition,
    Topic,
    TxnOffsetCommitRequestData,
)

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    nullableStringSerializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {
    0: [
        ("partition", int32Serializer),
        ("offset", int64Serializer),
        ("metadata", nullableStringSerializer),
        ("leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    1: [
        ("partition", int32Serializer),
        ("offset", int64Serializer),
        ("metadata", nullableStringSerializer),
        ("leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    2: [
        ("partition", int32Serializer),
        ("offset", int64Serializer),
        ("leader_epoch", int32Serializer),
        ("metadata", nullableStringSerializer),
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
}


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema)
    for version, schema in topicSchemas.items()
}


txnOffsetCommitRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("transactional_id", stringSerializer),
        ("group_id", stringSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
        ("topics", ArraySerializer(topicSerializers[0])),
    ],
    1: [
        ("transactional_id", stringSerializer),
        ("group_id", stringSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
        ("topics", ArraySerializer(topicSerializers[1])),
    ],
    2: [
        ("transactional_id", stringSerializer),
        ("group_id", stringSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
        ("topics", ArraySerializer(topicSerializers[2])),
    ],
}


txnOffsetCommitRequestDataSerializers: Dict[
    int, DataClassSerializer[TxnOffsetCommitRequestData]
] = {
    version: DataClassSerializer(TxnOffsetCommitRequestData, schema)
    for version, schema in txnOffsetCommitRequestDataSchemas.items()
}
