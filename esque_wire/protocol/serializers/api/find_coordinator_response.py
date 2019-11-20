##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.find_coordinator_response import FindCoordinatorResponseData

from ._main_serializers import (
    ClassSerializer,
    DummySerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


findCoordinatorResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
        ("error_message", DummySerializer(nullableStringSerializer.default)),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
    ],
    2: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
    ],
}


findCoordinatorResponseDataSerializers: Dict[int, ClassSerializer[FindCoordinatorResponseData]] = {
    version: ClassSerializer(FindCoordinatorResponseData, schema)
    for version, schema in findCoordinatorResponseDataSchemas.items()
}

findCoordinatorResponseDataSerializers[-1] = findCoordinatorResponseDataSerializers[2]
