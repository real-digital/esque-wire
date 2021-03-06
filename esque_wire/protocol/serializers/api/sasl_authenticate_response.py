###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.sasl_authenticate_response import SaslAuthenticateResponseData
from ._main_serializers import (
    ClassSerializer,
    DummySerializer,
    Schema,
    bytesSerializer,
    errorCodeSerializer,
    int64Serializer,
    nullableStringSerializer,
)

saslAuthenticateResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
        ("auth_bytes", bytesSerializer),
        ("session_lifetime_ms", DummySerializer(int64Serializer.default)),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("error_message", nullableStringSerializer),
        ("auth_bytes", bytesSerializer),
        ("session_lifetime_ms", int64Serializer),
    ],
}


saslAuthenticateResponseDataSerializers: Dict[int, ClassSerializer[SaslAuthenticateResponseData]] = {
    version: ClassSerializer(SaslAuthenticateResponseData, schema)
    for version, schema in saslAuthenticateResponseDataSchemas.items()
}

saslAuthenticateResponseDataSerializers[-1] = saslAuthenticateResponseDataSerializers[1]
