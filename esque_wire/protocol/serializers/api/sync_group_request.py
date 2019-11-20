##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.sync_group_request import Assignment, SyncGroupRequestData
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    bytesSerializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)

assignmentSchemas: Dict[int, Schema] = {
    0: [("member_id", stringSerializer), ("assignment", bytesSerializer)],
    1: [("member_id", stringSerializer), ("assignment", bytesSerializer)],
    2: [("member_id", stringSerializer), ("assignment", bytesSerializer)],
    3: [("member_id", stringSerializer), ("assignment", bytesSerializer)],
}


assignmentSerializers: Dict[int, ClassSerializer[Assignment]] = {
    version: ClassSerializer(Assignment, schema) for version, schema in assignmentSchemas.items()
}

assignmentSerializers[-1] = assignmentSerializers[3]


syncGroupRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("assignments", ArraySerializer(assignmentSerializers[0])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    1: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("assignments", ArraySerializer(assignmentSerializers[1])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    2: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("assignments", ArraySerializer(assignmentSerializers[2])),
        ("group_instance_id", DummySerializer(nullableStringSerializer.default)),
    ],
    3: [
        ("group_id", stringSerializer),
        ("generation_id", int32Serializer),
        ("member_id", stringSerializer),
        ("group_instance_id", nullableStringSerializer),
        ("assignments", ArraySerializer(assignmentSerializers[3])),
    ],
}


syncGroupRequestDataSerializers: Dict[int, ClassSerializer[SyncGroupRequestData]] = {
    version: ClassSerializer(SyncGroupRequestData, schema) for version, schema in syncGroupRequestDataSchemas.items()
}

syncGroupRequestDataSerializers[-1] = syncGroupRequestDataSerializers[3]
