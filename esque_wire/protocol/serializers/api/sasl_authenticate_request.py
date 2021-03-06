###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.sasl_authenticate_request import SaslAuthenticateRequestData
from ._main_serializers import ClassSerializer, Schema, bytesSerializer

saslAuthenticateRequestDataSchemas: Dict[int, Schema] = {
    0: [("auth_bytes", bytesSerializer)],
    1: [("auth_bytes", bytesSerializer)],
}


saslAuthenticateRequestDataSerializers: Dict[int, ClassSerializer[SaslAuthenticateRequestData]] = {
    version: ClassSerializer(SaslAuthenticateRequestData, schema)
    for version, schema in saslAuthenticateRequestDataSchemas.items()
}

saslAuthenticateRequestDataSerializers[-1] = saslAuthenticateRequestDataSerializers[1]
