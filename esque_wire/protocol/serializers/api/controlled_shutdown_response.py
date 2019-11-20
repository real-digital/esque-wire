##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.controlled_shutdown_response import (
    ControlledShutdownResponseData,
    RemainingPartition,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    stringSerializer,
)


remainingPartitionSchemas: Dict[int, Schema] = {
    0: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
    1: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
    2: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
}


remainingPartitionSerializers: Dict[int, DataClassSerializer[RemainingPartition]] = {
    version: DataClassSerializer(RemainingPartition, schema)
    for version, schema in remainingPartitionSchemas.items()
}


controlledShutdownResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("remaining_partitions", ArraySerializer(remainingPartitionSerializers[0])),
    ],
    1: [
        ("error_code", int16Serializer),
        ("remaining_partitions", ArraySerializer(remainingPartitionSerializers[1])),
    ],
    2: [
        ("error_code", int16Serializer),
        ("remaining_partitions", ArraySerializer(remainingPartitionSerializers[2])),
    ],
}


controlledShutdownResponseDataSerializers: Dict[
    int, DataClassSerializer[ControlledShutdownResponseData]
] = {
    version: DataClassSerializer(ControlledShutdownResponseData, schema)
    for version, schema in controlledShutdownResponseDataSchemas.items()
}