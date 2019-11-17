##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.end_txn_request import (
    EndTxnRequestData,
)

from esque_wire.protocol.serializers import (
    DataClassSerializer,
    Schema,
    booleanSerializer,
    int16Serializer,
    int64Serializer,
    stringSerializer,
)


endTxnRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ('transactional_id', stringSerializer),
        ('producer_id', int64Serializer),
        ('producer_epoch', int16Serializer),
        ('transaction_result', booleanSerializer),
    ],
    1: [
        ('transactional_id', stringSerializer),
        ('producer_id', int64Serializer),
        ('producer_epoch', int16Serializer),
        ('transaction_result', booleanSerializer),
    ],
}


endTxnRequestDataSerializers: Dict[int, DataClassSerializer[EndTxnRequestData]] = {
    version: DataClassSerializer(EndTxnRequestData, schema) for version, schema
    in endTxnRequestDataSchemas.items()
}

