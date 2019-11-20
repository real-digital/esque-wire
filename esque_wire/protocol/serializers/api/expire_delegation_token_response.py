##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.expire_delegation_token_response import (
    ExpireDelegationTokenResponseData,
)

from esque_wire.protocol.serializers import (
    DataClassSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
)


expireDelegationTokenResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("expiry_timestamp", int64Serializer),
        ("throttle_time_ms", int32Serializer),
    ],
    1: [
        ("error_code", int16Serializer),
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