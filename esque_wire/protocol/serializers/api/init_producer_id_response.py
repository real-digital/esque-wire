##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.init_producer_id_response import InitProducerIdResponseData

from ._main_serializers import (
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int16Serializer,
    int32Serializer,
    int64Serializer,
)


initProducerIdResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("producer_id", int64Serializer),
        ("producer_epoch", int16Serializer),
    ],
}


initProducerIdResponseDataSerializers: Dict[int, ClassSerializer[InitProducerIdResponseData]] = {
    version: ClassSerializer(InitProducerIdResponseData, schema)
    for version, schema in initProducerIdResponseDataSchemas.items()
}

initProducerIdResponseDataSerializers[-1] = initProducerIdResponseDataSerializers[1]
