###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.sasl_handshake_response import SaslHandshakeResponseData
from ._main_serializers import ArraySerializer, ClassSerializer, Schema, errorCodeSerializer, stringSerializer

saslHandshakeResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", errorCodeSerializer), ("mechanisms", ArraySerializer(stringSerializer))],
    1: [("error_code", errorCodeSerializer), ("mechanisms", ArraySerializer(stringSerializer))],
}


saslHandshakeResponseDataSerializers: Dict[int, ClassSerializer[SaslHandshakeResponseData]] = {
    version: ClassSerializer(SaslHandshakeResponseData, schema)
    for version, schema in saslHandshakeResponseDataSchemas.items()
}

saslHandshakeResponseDataSerializers[-1] = saslHandshakeResponseDataSerializers[1]
