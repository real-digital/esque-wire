##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.renew_delegation_token_response import (
    RenewDelegationTokenResponseData,
)

from esque_wire.protocol.serializers import (
    DataClassSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
)


renewDelegationTokenResponseDataSchemas: Dict[int, Schema] = {
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


renewDelegationTokenResponseDataSerializers: Dict[
    int, DataClassSerializer[RenewDelegationTokenResponseData]
] = {
    version: DataClassSerializer(RenewDelegationTokenResponseData, schema)
    for version, schema in renewDelegationTokenResponseDataSchemas.items()
}