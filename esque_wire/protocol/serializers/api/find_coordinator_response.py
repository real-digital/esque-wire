##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.find_coordinator_response import (
    FindCoordinatorResponseData,
)

from esque_wire.protocol.serializers import (
    DataClassSerializer,
    DummySerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


findCoordinatorResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ('error_code', int16Serializer),
        ('node_id', int32Serializer),
        ('host', stringSerializer),
        ('port', int32Serializer),
        ('throttle_time_ms', DummySerializer(int32Serializer.default)),
        ('error_message', DummySerializer(nullableStringSerializer.default)),
    ],
    1: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('error_message', nullableStringSerializer),
        ('node_id', int32Serializer),
        ('host', stringSerializer),
        ('port', int32Serializer),
    ],
    2: [
        ('throttle_time_ms', int32Serializer),
        ('error_code', int16Serializer),
        ('error_message', nullableStringSerializer),
        ('node_id', int32Serializer),
        ('host', stringSerializer),
        ('port', int32Serializer),
    ],
}


findCoordinatorResponseDataSerializers: Dict[int, DataClassSerializer[FindCoordinatorResponseData]] = {
    version: DataClassSerializer(FindCoordinatorResponseData, schema) for version, schema
    in findCoordinatorResponseDataSchemas.items()
}

