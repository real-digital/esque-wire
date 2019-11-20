##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.add_partitions_to_txn_request import (
    AddPartitionsToTxnRequestData,
    Topic,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)


topicSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
}


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema)
    for version, schema in topicSchemas.items()
}


addPartitionsToTxnRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("transactional_id", stringSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
        ("topics", ArraySerializer(topicSerializers[0])),
    ],
    1: [
        ("transactional_id", stringSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
        ("topics", ArraySerializer(topicSerializers[1])),
    ],
}


addPartitionsToTxnRequestDataSerializers: Dict[
    int, DataClassSerializer[AddPartitionsToTxnRequestData]
] = {
    version: DataClassSerializer(AddPartitionsToTxnRequestData, schema)
    for version, schema in addPartitionsToTxnRequestDataSchemas.items()
}
