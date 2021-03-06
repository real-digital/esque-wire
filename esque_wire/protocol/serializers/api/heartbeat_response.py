###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.heartbeat_response import HeartbeatResponseData
from ._main_serializers import ClassSerializer, DummySerializer, Schema, errorCodeSerializer, int32Serializer

heartbeatResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", errorCodeSerializer), ("throttle_time_ms", DummySerializer(int32Serializer.default))],
    1: [("throttle_time_ms", int32Serializer), ("error_code", errorCodeSerializer)],
    2: [("throttle_time_ms", int32Serializer), ("error_code", errorCodeSerializer)],
    3: [("throttle_time_ms", int32Serializer), ("error_code", errorCodeSerializer)],
}


heartbeatResponseDataSerializers: Dict[int, ClassSerializer[HeartbeatResponseData]] = {
    version: ClassSerializer(HeartbeatResponseData, schema) for version, schema in heartbeatResponseDataSchemas.items()
}

heartbeatResponseDataSerializers[-1] = heartbeatResponseDataSerializers[3]
