##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.delete_groups_response import (
    DeleteGroupsResponseData,
    GroupErrorCode,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    stringSerializer,
)


groupErrorCodeSchemas: Dict[int, Schema] = {
    0: [("group_id", stringSerializer), ("error_code", int16Serializer)],
    1: [("group_id", stringSerializer), ("error_code", int16Serializer)],
}


groupErrorCodeSerializers: Dict[int, DataClassSerializer[GroupErrorCode]] = {
    version: DataClassSerializer(GroupErrorCode, schema)
    for version, schema in groupErrorCodeSchemas.items()
}


deleteGroupsResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("group_error_codes", ArraySerializer(groupErrorCodeSerializers[0])),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("group_error_codes", ArraySerializer(groupErrorCodeSerializers[1])),
    ],
}


deleteGroupsResponseDataSerializers: Dict[
    int, DataClassSerializer[DeleteGroupsResponseData]
] = {
    version: DataClassSerializer(DeleteGroupsResponseData, schema)
    for version, schema in deleteGroupsResponseDataSchemas.items()
}
