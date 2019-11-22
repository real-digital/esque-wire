###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.renew_delegation_token_request import RenewDelegationTokenRequestData
from ._main_serializers import ClassSerializer, Schema, bytesSerializer, int64Serializer

renewDelegationTokenRequestDataSchemas: Dict[int, Schema] = {
    0: [("hmac", bytesSerializer), ("renew_time_period", int64Serializer)],
    1: [("hmac", bytesSerializer), ("renew_time_period", int64Serializer)],
}


renewDelegationTokenRequestDataSerializers: Dict[int, ClassSerializer[RenewDelegationTokenRequestData]] = {
    version: ClassSerializer(RenewDelegationTokenRequestData, schema)
    for version, schema in renewDelegationTokenRequestDataSchemas.items()
}

renewDelegationTokenRequestDataSerializers[-1] = renewDelegationTokenRequestDataSerializers[1]
