##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.add_partitions_to_txn_response import (
    AddPartitionsToTxnResponseData,
    Error,
    PartitionError,
)

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    stringSerializer,
)


partitionErrorSchemas: Dict[int, Schema] = {
    0: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
    1: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
}


partitionErrorSerializers: Dict[int, DataClassSerializer[PartitionError]] = {
    version: DataClassSerializer(PartitionError, schema)
    for version, schema in partitionErrorSchemas.items()
}


errorSchemas: Dict[int, Schema] = {
    0: [
        ("topic", stringSerializer),
        ("partition_errors", ArraySerializer(partitionErrorSerializers[0])),
    ],
    1: [
        ("topic", stringSerializer),
        ("partition_errors", ArraySerializer(partitionErrorSerializers[1])),
    ],
}


errorSerializers: Dict[int, DataClassSerializer[Error]] = {
    version: DataClassSerializer(Error, schema)
    for version, schema in errorSchemas.items()
}


addPartitionsToTxnResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("errors", ArraySerializer(errorSerializers[0])),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("errors", ArraySerializer(errorSerializers[1])),
    ],
}


addPartitionsToTxnResponseDataSerializers: Dict[
    int, DataClassSerializer[AddPartitionsToTxnResponseData]
] = {
    version: DataClassSerializer(AddPartitionsToTxnResponseData, schema)
    for version, schema in addPartitionsToTxnResponseDataSchemas.items()
}
