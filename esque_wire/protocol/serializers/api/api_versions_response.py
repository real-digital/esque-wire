###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.api_versions_response import ApiVersion, ApiVersionsResponseData
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    apiKeySerializer,
    errorCodeSerializer,
    int16Serializer,
    int32Serializer,
)

apiVersionSchemas: Dict[int, Schema] = {
    0: [("api_key", apiKeySerializer), ("min_version", int16Serializer), ("max_version", int16Serializer)],
    1: [("api_key", apiKeySerializer), ("min_version", int16Serializer), ("max_version", int16Serializer)],
    2: [("api_key", apiKeySerializer), ("min_version", int16Serializer), ("max_version", int16Serializer)],
}


apiVersionSerializers: Dict[int, ClassSerializer[ApiVersion]] = {
    version: ClassSerializer(ApiVersion, schema) for version, schema in apiVersionSchemas.items()
}

apiVersionSerializers[-1] = apiVersionSerializers[2]


apiVersionsResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("api_versions", ArraySerializer(apiVersionSerializers[0])),
        ("throttle_time_ms", DummySerializer(0)),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("api_versions", ArraySerializer(apiVersionSerializers[1])),
        ("throttle_time_ms", int32Serializer),
    ],
    2: [
        ("error_code", errorCodeSerializer),
        ("api_versions", ArraySerializer(apiVersionSerializers[2])),
        ("throttle_time_ms", int32Serializer),
    ],
}


apiVersionsResponseDataSerializers: Dict[int, ClassSerializer[ApiVersionsResponseData]] = {
    version: ClassSerializer(ApiVersionsResponseData, schema)
    for version, schema in apiVersionsResponseDataSchemas.items()
}

apiVersionsResponseDataSerializers[-1] = apiVersionsResponseDataSerializers[2]
