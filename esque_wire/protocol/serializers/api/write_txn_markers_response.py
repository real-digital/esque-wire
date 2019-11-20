##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.write_txn_markers_response import Partition, Topic, TransactionMarker, WriteTxnMarkersResponseData

from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {0: [("partition", int32Serializer), ("error_code", errorCodeSerializer)]}


partitionSerializers: Dict[int, ClassSerializer[Partition]] = {
    version: ClassSerializer(Partition, schema) for version, schema in partitionSchemas.items()
}

partitionSerializers[-1] = partitionSerializers[0]


topicSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[0]))]
}


topicSerializers: Dict[int, ClassSerializer[Topic]] = {
    version: ClassSerializer(Topic, schema) for version, schema in topicSchemas.items()
}

topicSerializers[-1] = topicSerializers[0]


transactionMarkerSchemas: Dict[int, Schema] = {
    0: [("producer_id", int64Serializer), ("topics", ArraySerializer(topicSerializers[0]))]
}


transactionMarkerSerializers: Dict[int, ClassSerializer[TransactionMarker]] = {
    version: ClassSerializer(TransactionMarker, schema) for version, schema in transactionMarkerSchemas.items()
}

transactionMarkerSerializers[-1] = transactionMarkerSerializers[0]


writeTxnMarkersResponseDataSchemas: Dict[int, Schema] = {
    0: [("transaction_markers", ArraySerializer(transactionMarkerSerializers[0]))]
}


writeTxnMarkersResponseDataSerializers: Dict[int, ClassSerializer[WriteTxnMarkersResponseData]] = {
    version: ClassSerializer(WriteTxnMarkersResponseData, schema)
    for version, schema in writeTxnMarkersResponseDataSchemas.items()
}

writeTxnMarkersResponseDataSerializers[-1] = writeTxnMarkersResponseDataSerializers[0]
