###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.controlled_shutdown_response import ControlledShutdownResponseData, RemainingPartition
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    stringSerializer,
)

remainingPartitionSchemas: Dict[int, Schema] = {
    0: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
    1: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
    2: [("topic_name", stringSerializer), ("partition_index", int32Serializer)],
}


remainingPartitionSerializers: Dict[int, ClassSerializer[RemainingPartition]] = {
    version: ClassSerializer(RemainingPartition, schema) for version, schema in remainingPartitionSchemas.items()
}

remainingPartitionSerializers[-1] = remainingPartitionSerializers[2]


controlledShutdownResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("remaining_partitions", ArraySerializer(remainingPartitionSerializers[0])),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("remaining_partitions", ArraySerializer(remainingPartitionSerializers[1])),
    ],
    2: [
        ("error_code", errorCodeSerializer),
        ("remaining_partitions", ArraySerializer(remainingPartitionSerializers[2])),
    ],
}


controlledShutdownResponseDataSerializers: Dict[int, ClassSerializer[ControlledShutdownResponseData]] = {
    version: ClassSerializer(ControlledShutdownResponseData, schema)
    for version, schema in controlledShutdownResponseDataSchemas.items()
}

controlledShutdownResponseDataSerializers[-1] = controlledShutdownResponseDataSerializers[2]
