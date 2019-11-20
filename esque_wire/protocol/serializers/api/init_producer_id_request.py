##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.init_producer_id_request import InitProducerIdRequestData
from ._main_serializers import ClassSerializer, Schema, int32Serializer, nullableStringSerializer

initProducerIdRequestDataSchemas: Dict[int, Schema] = {
    0: [("transactional_id", nullableStringSerializer), ("transaction_timeout_ms", int32Serializer)],
    1: [("transactional_id", nullableStringSerializer), ("transaction_timeout_ms", int32Serializer)],
}


initProducerIdRequestDataSerializers: Dict[int, ClassSerializer[InitProducerIdRequestData]] = {
    version: ClassSerializer(InitProducerIdRequestData, schema)
    for version, schema in initProducerIdRequestDataSchemas.items()
}

initProducerIdRequestDataSerializers[-1] = initProducerIdRequestDataSerializers[1]
