##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.sasl_authenticate_request import (
    SaslAuthenticateRequestData,
)

from esque_wire.protocol.serializers import DataClassSerializer, Schema, bytesSerializer


saslAuthenticateRequestDataSchemas: Dict[int, Schema] = {
    0: [("auth_bytes", bytesSerializer)],
    1: [("auth_bytes", bytesSerializer)],
}


saslAuthenticateRequestDataSerializers: Dict[
    int, DataClassSerializer[SaslAuthenticateRequestData]
] = {
    version: DataClassSerializer(SaslAuthenticateRequestData, schema)
    for version, schema in saslAuthenticateRequestDataSchemas.items()
}