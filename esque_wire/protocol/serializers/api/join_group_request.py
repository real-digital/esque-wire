##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.join_group_request import JoinGroupRequestData, Protocol

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    bytesSerializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


protocolSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer), ("metadata", bytesSerializer)],
    1: [("name", stringSerializer), ("metadata", bytesSerializer)],
    2: [("name", stringSerializer), ("metadata", bytesSerializer)],
    3: [("name", stringSerializer), ("metadata", bytesSerializer)],
    4: [("name", stringSerializer), ("metadata", bytesSerializer)],
    5: [("name", stringSerializer), ("metadata", bytesSerializer)],
}


protocolSerializers: Dict[int, DataClassSerializer[Protocol]] = {
    version: DataClassSerializer(Protocol, schema)
    for version, schema in protocolSchemas.items()
}


joinGroupRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("group_id", stringSerializer),
        ("session_timeout_ms", int32Serializer),
        ("member_id", stringSerializer),
        ("protocol_type", stringSerializer),
        ("protocols", ArraySerializer(protocolSerializers[0])),
        ("rebalance_timeout_ms", DummySerializer(int32Serializer.default)),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    1: [
        ("group_id", stringSerializer),
        ("session_timeout_ms", int32Serializer),
        ("rebalance_timeout_ms", int32Serializer),
        ("member_id", stringSerializer),
        ("protocol_type", stringSerializer),
        ("protocols", ArraySerializer(protocolSerializers[1])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    2: [
        ("group_id", stringSerializer),
        ("session_timeout_ms", int32Serializer),
        ("rebalance_timeout_ms", int32Serializer),
        ("member_id", stringSerializer),
        ("protocol_type", stringSerializer),
        ("protocols", ArraySerializer(protocolSerializers[2])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    3: [
        ("group_id", stringSerializer),
        ("session_timeout_ms", int32Serializer),
        ("rebalance_timeout_ms", int32Serializer),
        ("member_id", stringSerializer),
        ("protocol_type", stringSerializer),
        ("protocols", ArraySerializer(protocolSerializers[3])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    4: [
        ("group_id", stringSerializer),
        ("session_timeout_ms", int32Serializer),
        ("rebalance_timeout_ms", int32Serializer),
        ("member_id", stringSerializer),
        ("protocol_type", stringSerializer),
        ("protocols", ArraySerializer(protocolSerializers[4])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    5: [
        ("group_id", stringSerializer),
        ("session_timeout_ms", int32Serializer),
        ("rebalance_timeout_ms", int32Serializer),
        ("member_id", stringSerializer),
        ("group_instance_id", nullableStringSerializer),
        ("protocol_type", stringSerializer),
        ("protocols", ArraySerializer(protocolSerializers[5])),
    ],
}


joinGroupRequestDataSerializers: Dict[
    int, DataClassSerializer[JoinGroupRequestData]
] = {
    version: DataClassSerializer(JoinGroupRequestData, schema)
    for version, schema in joinGroupRequestDataSchemas.items()
}
