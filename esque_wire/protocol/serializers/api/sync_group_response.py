##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.sync_group_response import SyncGroupResponseData

from ._main_serializers import (
    DataClassSerializer,
    DummySerializer,
    Schema,
    bytesSerializer,
    errorCodeSerializer,
    int32Serializer,
)


syncGroupResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("assignment", bytesSerializer),
        ("throttle_time_ms", DummySerializer(int32Serializer.default)),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("assignment", bytesSerializer),
    ],
    2: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("assignment", bytesSerializer),
    ],
    3: [
        ("throttle_time_ms", int32Serializer),
        ("error_code", errorCodeSerializer),
        ("assignment", bytesSerializer),
    ],
}


syncGroupResponseDataSerializers: Dict[
    int, DataClassSerializer[SyncGroupResponseData]
] = {
    version: DataClassSerializer(SyncGroupResponseData, schema)
    for version, schema in syncGroupResponseDataSchemas.items()
}
