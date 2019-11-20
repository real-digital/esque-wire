##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.txn_offset_commit_response import (
    Partition,
    Topic,
    TxnOffsetCommitResponseData,
)

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {
    0: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
    1: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
    2: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
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


txnOffsetCommitResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[0])),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[1])),
    ],
    2: [
        ("throttle_time_ms", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[2])),
    ],
}


txnOffsetCommitResponseDataSerializers: Dict[
    int, DataClassSerializer[TxnOffsetCommitResponseData]
] = {
    version: DataClassSerializer(TxnOffsetCommitResponseData, schema)
    for version, schema in txnOffsetCommitResponseDataSchemas.items()
}
