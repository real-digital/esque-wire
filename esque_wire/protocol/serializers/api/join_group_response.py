##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.join_group_response import JoinGroupResponseData, Member
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    bytesSerializer,
    errorCodeSerializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)

memberSchemas: Dict[int, Schema] = {
    0: [
        ("member_id", stringSerializer),
        ("metadata", bytesSerializer),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    1: [
        ("member_id", stringSerializer),
        ("metadata", bytesSerializer),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    2: [
        ("member_id", stringSerializer),
        ("metadata", bytesSerializer),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    3: [
        ("member_id", stringSerializer),
        ("metadata", bytesSerializer),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    4: [
        ("member_id", stringSerializer),
        ("metadata", bytesSerializer),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    5: [
        ("member_id", stringSerializer),
        ("group_instance_id", nullableStringSerializer),
        ("metadata", bytesSerializer),
    ],
}


memberSerializers: Dict[int, ClassSerializer[Member]] = {
    version: ClassSerializer(Member, schema) for version, schema in memberSchemas.items()
}

memberSerializers[-1] = memberSerializers[5]


joinGroupResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("generation_id", int32Serializer),
        ("protocol_name", stringSerializer),
        ("leader", stringSerializer),
        ("member_id", stringSerializer),
        ("members", ArraySerializer(memberSerializers[0])),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("generation_id", int32Serializer),
        ("protocol_name", stringSerializer),
        ("leader", stringSerializer),
        ("member_id", stringSerializer),
        ("members", ArraySerializer(memberSerializers[1])),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    2: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("generation_id", int32Serializer),
        ("protocol_name", stringSerializer),
        ("leader", stringSerializer),
        ("member_id", stringSerializer),
        ("members", ArraySerializer(memberSerializers[2])),
    ],
    3: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("generation_id", int32Serializer),
        ("protocol_name", stringSerializer),
        ("leader", stringSerializer),
        ("member_id", stringSerializer),
        ("members", ArraySerializer(memberSerializers[3])),
    ],
    4: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("generation_id", int32Serializer),
        ("protocol_name", stringSerializer),
        ("leader", stringSerializer),
        ("member_id", stringSerializer),
        ("members", ArraySerializer(memberSerializers[4])),
    ],
    5: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("generation_id", int32Serializer),
        ("protocol_name", stringSerializer),
        ("leader", stringSerializer),
        ("member_id", stringSerializer),
        ("members", ArraySerializer(memberSerializers[5])),
    ],
}


joinGroupResponseDataSerializers: Dict[int, ClassSerializer[JoinGroupResponseData]] = {
    version: ClassSerializer(JoinGroupResponseData, schema) for version, schema in joinGroupResponseDataSchemas.items()
}

joinGroupResponseDataSerializers[-1] = joinGroupResponseDataSerializers[5]
