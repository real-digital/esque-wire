##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.delete_groups_response import DeleteGroupsResponseData, GroupErrorCode

from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    stringSerializer,
)


groupErrorCodeSchemas: Dict[int, Schema] = {
    0: [("group_id", stringSerializer), ("error_code", errorCodeSerializer)],
    1: [("group_id", stringSerializer), ("error_code", errorCodeSerializer)],
}


groupErrorCodeSerializers: Dict[int, ClassSerializer[GroupErrorCode]] = {
    version: ClassSerializer(GroupErrorCode, schema) for version, schema in groupErrorCodeSchemas.items()
}

groupErrorCodeSerializers[-1] = groupErrorCodeSerializers[1]


deleteGroupsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("group_error_codes", ArraySerializer(groupErrorCodeSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("group_error_codes", ArraySerializer(groupErrorCodeSerializers[1]))],
}


deleteGroupsResponseDataSerializers: Dict[int, ClassSerializer[DeleteGroupsResponseData]] = {
    version: ClassSerializer(DeleteGroupsResponseData, schema)
    for version, schema in deleteGroupsResponseDataSchemas.items()
}

deleteGroupsResponseDataSerializers[-1] = deleteGroupsResponseDataSerializers[1]
