##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.alter_replica_log_dirs_response import AlterReplicaLogDirsResponseData, Partition, Topic

from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {
    0: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
    1: [("partition", int32Serializer), ("error_code", errorCodeSerializer)],
}


partitionSerializers: Dict[int, ClassSerializer[Partition]] = {
    version: ClassSerializer(Partition, schema) for version, schema in partitionSchemas.items()
}

partitionSerializers[-1] = partitionSerializers[1]


topicSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[0]))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[1]))],
}


topicSerializers: Dict[int, ClassSerializer[Topic]] = {
    version: ClassSerializer(Topic, schema) for version, schema in topicSchemas.items()
}

topicSerializers[-1] = topicSerializers[1]


alterReplicaLogDirsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("topics", ArraySerializer(topicSerializers[1]))],
}


alterReplicaLogDirsResponseDataSerializers: Dict[int, ClassSerializer[AlterReplicaLogDirsResponseData]] = {
    version: ClassSerializer(AlterReplicaLogDirsResponseData, schema)
    for version, schema in alterReplicaLogDirsResponseDataSchemas.items()
}

alterReplicaLogDirsResponseDataSerializers[-1] = alterReplicaLogDirsResponseDataSerializers[1]
