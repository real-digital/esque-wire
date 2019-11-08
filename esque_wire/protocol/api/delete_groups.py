# FIXME autogenerated module, check for errors!
from typing import Dict, List

from dataclasses import dataclass

from esque_wire.protocol.api.base import ApiKey, RequestData, ResponseData
from esque_wire.protocol.serializers import (
    ArraySerializer,
    BaseSerializer,
    NamedTupleSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    stringSerializer,
)


@dataclass
class DeleteGroupsRequestData(RequestData):
    # An array of groups to be deleted.
    groups: List["str"]  # STRING

    @staticmethod
    def api_key() -> int:
        return ApiKey.DELETE_GROUPS  # == 42


@dataclass
class GroupErrorCodes:
    # The unique group identifier
    group_id: "str"  # STRING

    # Response error code
    error_code: "int"  # INT16


@dataclass
class DeleteGroupsResponseData(ResponseData):
    # Duration in milliseconds for which the request was throttled due to quota violation (Zero if the
    # request did not violate any quota)
    throttle_time_ms: "int"  # INT32

    # An array of per group error codes.
    group_error_codes: List["GroupErrorCodes"]

    @staticmethod
    def api_key() -> int:
        return ApiKey.DELETE_GROUPS  # == 42


deleteGroupsRequestDataSchemas: Dict[int, Schema] = {
    0: [("groups", ArraySerializer(stringSerializer))],
    1: [("groups", ArraySerializer(stringSerializer))],
}


deleteGroupsRequestDataSerializers: Dict[int, BaseSerializer[DeleteGroupsRequestData]] = {
    version: NamedTupleSerializer(DeleteGroupsRequestData, schema)
    for version, schema in deleteGroupsRequestDataSchemas.items()
}


groupErrorCodesSchemas: Dict[int, Schema] = {
    0: [("group_id", stringSerializer), ("error_code", int16Serializer)],
    1: [("group_id", stringSerializer), ("error_code", int16Serializer)],
}


groupErrorCodesSerializers: Dict[int, BaseSerializer[GroupErrorCodes]] = {
    version: NamedTupleSerializer(GroupErrorCodes, schema) for version, schema in groupErrorCodesSchemas.items()
}


deleteGroupsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("group_error_codes", ArraySerializer(groupErrorCodesSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("group_error_codes", ArraySerializer(groupErrorCodesSerializers[1]))],
}


deleteGroupsResponseDataSerializers: Dict[int, BaseSerializer[DeleteGroupsResponseData]] = {
    version: NamedTupleSerializer(DeleteGroupsResponseData, schema)
    for version, schema in deleteGroupsResponseDataSchemas.items()
}