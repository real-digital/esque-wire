##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.create_delegation_token_request import (
    CreateDelegationTokenRequestData,
    Renewer,
)

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    int64Serializer,
    stringSerializer,
)


renewerSchemas: Dict[int, Schema] = {
    0: [("principal_type", stringSerializer), ("name", stringSerializer)],
    1: [("principal_type", stringSerializer), ("name", stringSerializer)],
}


renewerSerializers: Dict[int, DataClassSerializer[Renewer]] = {
    version: DataClassSerializer(Renewer, schema)
    for version, schema in renewerSchemas.items()
}


createDelegationTokenRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("renewers", ArraySerializer(renewerSerializers[0])),
        ("max_life_time", int64Serializer),
    ],
    1: [
        ("renewers", ArraySerializer(renewerSerializers[1])),
        ("max_life_time", int64Serializer),
    ],
}


createDelegationTokenRequestDataSerializers: Dict[
    int, DataClassSerializer[CreateDelegationTokenRequestData]
] = {
    version: DataClassSerializer(CreateDelegationTokenRequestData, schema)
    for version, schema in createDelegationTokenRequestDataSchemas.items()
}
