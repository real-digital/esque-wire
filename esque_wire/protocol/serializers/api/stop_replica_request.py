###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.stop_replica_request import Partition, StopReplicaRequestData
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    booleanSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)

partitionSchemas: Dict[int, Schema] = {
    0: [
        ("topic", stringSerializer),
        (None, int32Serializer),
        ("partition_ids", DummySerializer(ArraySerializer(int32Serializer).default)),
    ],
    1: [("topic", stringSerializer), ("partition_ids", ArraySerializer(int32Serializer))],
}


partitionSerializers: Dict[int, ClassSerializer[Partition]] = {
    version: ClassSerializer(Partition, schema) for version, schema in partitionSchemas.items()
}

partitionSerializers[-1] = partitionSerializers[1]


stopReplicaRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("delete_partitions", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[0])),
        ("broker_epoch", DummySerializer(int64Serializer.default)),
    ],
    1: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("broker_epoch", int64Serializer),
        ("delete_partitions", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[1])),
    ],
}


stopReplicaRequestDataSerializers: Dict[int, ClassSerializer[StopReplicaRequestData]] = {
    version: ClassSerializer(StopReplicaRequestData, schema)
    for version, schema in stopReplicaRequestDataSchemas.items()
}

stopReplicaRequestDataSerializers[-1] = stopReplicaRequestDataSerializers[1]
