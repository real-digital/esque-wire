###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.leave_group_response import LeaveGroupResponseData
from ._main_serializers import ClassSerializer, DummySerializer, Schema, errorCodeSerializer, int32Serializer

leaveGroupResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", errorCodeSerializer), ("throttle_time_ms", DummySerializer(int32Serializer.default))],
    1: [("throttle_time_ms", int32Serializer), ("error_code", errorCodeSerializer)],
    2: [("throttle_time_ms", int32Serializer), ("error_code", errorCodeSerializer)],
}


leaveGroupResponseDataSerializers: Dict[int, ClassSerializer[LeaveGroupResponseData]] = {
    version: ClassSerializer(LeaveGroupResponseData, schema)
    for version, schema in leaveGroupResponseDataSchemas.items()
}

leaveGroupResponseDataSerializers[-1] = leaveGroupResponseDataSerializers[2]
