###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.describe_delegation_token_response import (
    DescribeDelegationTokenResponseData,
    Owner,
    Renewer,
    TokenDetail,
)
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    bytesSerializer,
    errorCodeSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)

renewerSchemas: Dict[int, Schema] = {
    0: [("principal_type", stringSerializer), ("name", stringSerializer)],
    1: [("principal_type", stringSerializer), ("name", stringSerializer)],
}


renewerSerializers: Dict[int, ClassSerializer[Renewer]] = {
    version: ClassSerializer(Renewer, schema) for version, schema in renewerSchemas.items()
}

renewerSerializers[-1] = renewerSerializers[1]


ownerSchemas: Dict[int, Schema] = {
    0: [("principal_type", stringSerializer), ("name", stringSerializer)],
    1: [("principal_type", stringSerializer), ("name", stringSerializer)],
}


ownerSerializers: Dict[int, ClassSerializer[Owner]] = {
    version: ClassSerializer(Owner, schema) for version, schema in ownerSchemas.items()
}

ownerSerializers[-1] = ownerSerializers[1]


tokenDetailSchemas: Dict[int, Schema] = {
    0: [
        ("owner", ownerSerializers[0]),
        ("issue_timestamp", int64Serializer),
        ("expiry_timestamp", int64Serializer),
        ("max_timestamp", int64Serializer),
        ("token_id", stringSerializer),
        ("hmac", bytesSerializer),
        ("renewers", ArraySerializer(renewerSerializers[0])),
    ],
    1: [
        ("owner", ownerSerializers[1]),
        ("issue_timestamp", int64Serializer),
        ("expiry_timestamp", int64Serializer),
        ("max_timestamp", int64Serializer),
        ("token_id", stringSerializer),
        ("hmac", bytesSerializer),
        ("renewers", ArraySerializer(renewerSerializers[1])),
    ],
}


tokenDetailSerializers: Dict[int, ClassSerializer[TokenDetail]] = {
    version: ClassSerializer(TokenDetail, schema) for version, schema in tokenDetailSchemas.items()
}

tokenDetailSerializers[-1] = tokenDetailSerializers[1]


describeDelegationTokenResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("token_details", ArraySerializer(tokenDetailSerializers[0])),
        ("throttle_time_ms", int32Serializer),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("token_details", ArraySerializer(tokenDetailSerializers[1])),
        ("throttle_time_ms", int32Serializer),
    ],
}


describeDelegationTokenResponseDataSerializers: Dict[int, ClassSerializer[DescribeDelegationTokenResponseData]] = {
    version: ClassSerializer(DescribeDelegationTokenResponseData, schema)
    for version, schema in describeDelegationTokenResponseDataSchemas.items()
}

describeDelegationTokenResponseDataSerializers[-1] = describeDelegationTokenResponseDataSerializers[1]
