###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.create_delegation_token_response import CreateDelegationTokenResponseData, Owner
from ._main_serializers import (
    ClassSerializer,
    Schema,
    bytesSerializer,
    errorCodeSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)

ownerSchemas: Dict[int, Schema] = {
    0: [("principal_type", stringSerializer), ("name", stringSerializer)],
    1: [("principal_type", stringSerializer), ("name", stringSerializer)],
}


ownerSerializers: Dict[int, ClassSerializer[Owner]] = {
    version: ClassSerializer(Owner, schema) for version, schema in ownerSchemas.items()
}

ownerSerializers[-1] = ownerSerializers[1]


createDelegationTokenResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("owner", ownerSerializers[0]),
        ("issue_timestamp", int64Serializer),
        ("expiry_timestamp", int64Serializer),
        ("max_timestamp", int64Serializer),
        ("token_id", stringSerializer),
        ("hmac", bytesSerializer),
        ("throttle_time_ms", int32Serializer),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("owner", ownerSerializers[1]),
        ("issue_timestamp", int64Serializer),
        ("expiry_timestamp", int64Serializer),
        ("max_timestamp", int64Serializer),
        ("token_id", stringSerializer),
        ("hmac", bytesSerializer),
        ("throttle_time_ms", int32Serializer),
    ],
}


createDelegationTokenResponseDataSerializers: Dict[int, ClassSerializer[CreateDelegationTokenResponseData]] = {
    version: ClassSerializer(CreateDelegationTokenResponseData, schema)
    for version, schema in createDelegationTokenResponseDataSchemas.items()
}

createDelegationTokenResponseDataSerializers[-1] = createDelegationTokenResponseDataSerializers[1]
