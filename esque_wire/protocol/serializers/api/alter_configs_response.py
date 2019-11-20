##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.alter_configs_response import AlterConfigsResponseData, Resource

from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    nullableStringSerializer,
    resourceTypeSerializer,
    stringSerializer,
)


resourceSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", resourceTypeSerializer),
        ("resource_name", stringSerializer),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
        ("resource_type", resourceTypeSerializer),
        ("resource_name", stringSerializer),
    ],
}


resourceSerializers: Dict[int, ClassSerializer[Resource]] = {
    version: ClassSerializer(Resource, schema) for version, schema in resourceSchemas.items()
}

resourceSerializers[-1] = resourceSerializers[1]


alterConfigsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("resources", ArraySerializer(resourceSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("resources", ArraySerializer(resourceSerializers[1]))],
}


alterConfigsResponseDataSerializers: Dict[int, ClassSerializer[AlterConfigsResponseData]] = {
    version: ClassSerializer(AlterConfigsResponseData, schema)
    for version, schema in alterConfigsResponseDataSchemas.items()
}

alterConfigsResponseDataSerializers[-1] = alterConfigsResponseDataSerializers[1]
