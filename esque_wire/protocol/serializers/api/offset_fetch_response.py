##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.offset_fetch_response import (
    OffsetFetchResponseData,
    PartitionResponse,
    Response,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    nullableStringSerializer,
    stringSerializer,
)


partitionResponseSchemas: Dict[int, Schema] = {
    0: [
        ('partition', int32Serializer),
        ('offset', int64Serializer),
        ('metadata', nullableStringSerializer),
        ('error_code', int16Serializer),
        ('leader_epoch', DummySerializer(int32Serializer.default)),
    ],
    1: [
        ('partition', int32Serializer),
        ('offset', int64Serializer),
        ('metadata', nullableStringSerializer),
        ('error_code', int16Serializer),
        ('leader_epoch', DummySerializer(int32Serializer.default)),
    ],
    2: [
        ('partition', int32Serializer),
        ('offset', int64Serializer),
        ('metadata', nullableStringSerializer),
        ('error_code', int16Serializer),
        ('leader_epoch', DummySerializer(int32Serializer.default)),
    ],
    3: [
        ('partition', int32Serializer),
        ('offset', int64Serializer),
        ('metadata', nullableStringSerializer),
        ('error_code', int16Serializer),
        ('leader_epoch', DummySerializer(int32Serializer.default)),
    ],
    4: [
        ('partition', int32Serializer),
        ('offset', int64Serializer),
        ('metadata', nullableStringSerializer),
        ('error_code', int16Serializer),
        ('leader_epoch', DummySerializer(int32Serializer.default)),
    ],
    5: [
        ('partition', int32Serializer),
        ('offset', int64Serializer),
        ('leader_epoch', int32Serializer),
        ('metadata', nullableStringSerializer),
        ('error_code', int16Serializer),
    ],
}


partitionResponseSerializers: Dict[int, DataClassSerializer[PartitionResponse]] = {
    version: DataClassSerializer(PartitionResponse, schema) for version, schema
    in partitionResponseSchemas.items()
}


responseSchemas: Dict[int, Schema] = {
    0: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[0])),
    ],
    1: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[1])),
    ],
    2: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[2])),
    ],
    3: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[3])),
    ],
    4: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[4])),
    ],
    5: [
        ('topic', stringSerializer),
        ('partition_responses', ArraySerializer(partitionResponseSerializers[5])),
    ],
}


responseSerializers: Dict[int, DataClassSerializer[Response]] = {
    version: DataClassSerializer(Response, schema) for version, schema
    in responseSchemas.items()
}


offsetFetchResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ('responses', ArraySerializer(responseSerializers[0])),
        ('throttle_time_ms', DummySerializer(0)),
        ('error_code', DummySerializer(int16Serializer.default)),
    ],
    1: [
        ('responses', ArraySerializer(responseSerializers[1])),
        ('throttle_time_ms', DummySerializer(0)),
        ('error_code', DummySerializer(int16Serializer.default)),
    ],
    2: [
        ('responses', ArraySerializer(responseSerializers[2])),
        ('error_code', int16Serializer),
        ('throttle_time_ms', DummySerializer(0)),
    ],
    3: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[3])),
        ('error_code', int16Serializer),
    ],
    4: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[4])),
        ('error_code', int16Serializer),
    ],
    5: [
        ('throttle_time_ms', int32Serializer),
        ('responses', ArraySerializer(responseSerializers[5])),
        ('error_code', int16Serializer),
    ],
}


offsetFetchResponseDataSerializers: Dict[int, DataClassSerializer[OffsetFetchResponseData]] = {
    version: DataClassSerializer(OffsetFetchResponseData, schema) for version, schema
    in offsetFetchResponseDataSchemas.items()
}

