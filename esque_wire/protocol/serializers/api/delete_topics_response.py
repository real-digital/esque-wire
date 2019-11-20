##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.delete_topics_response import DeleteTopicsResponseData, Response
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    stringSerializer,
)

responseSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("error_code", errorCodeSerializer)],
    1: [("name", stringSerializer), ("error_code", errorCodeSerializer)],
    2: [("name", stringSerializer), ("error_code", errorCodeSerializer)],
    3: [("name", stringSerializer), ("error_code", errorCodeSerializer)],
}


responseSerializers: Dict[int, ClassSerializer[Response]] = {
    version: ClassSerializer(Response, schema) for version, schema in responseSchemas.items()
}

responseSerializers[-1] = responseSerializers[3]


deleteTopicsResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("responses", ArraySerializer(responseSerializers[0])),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    1: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responseSerializers[1]))],
    2: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responseSerializers[2]))],
    3: [("throttle_time_ms", int32Serializer), ("responses", ArraySerializer(responseSerializers[3]))],
}


deleteTopicsResponseDataSerializers: Dict[int, ClassSerializer[DeleteTopicsResponseData]] = {
    version: ClassSerializer(DeleteTopicsResponseData, schema)
    for version, schema in deleteTopicsResponseDataSchemas.items()
}

deleteTopicsResponseDataSerializers[-1] = deleteTopicsResponseDataSerializers[3]
