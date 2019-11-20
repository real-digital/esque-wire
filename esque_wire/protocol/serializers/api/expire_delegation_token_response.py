##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.expire_delegation_token_response import (
    ExpireDelegationTokenResponseData,
)

from ._main_serializers import (
    DataClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    int64Serializer,
)


expireDelegationTokenResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("expiry_timestamp", int64Serializer),
        ("throttle_time_ms", int32Serializer),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("expiry_timestamp", int64Serializer),
        ("throttle_time_ms", int32Serializer),
    ],
}


expireDelegationTokenResponseDataSerializers: Dict[
    int, DataClassSerializer[ExpireDelegationTokenResponseData]
] = {
    version: DataClassSerializer(ExpireDelegationTokenResponseData, schema)
    for version, schema in expireDelegationTokenResponseDataSchemas.items()
}
