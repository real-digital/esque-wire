##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.alter_replica_log_dirs_request import (
    AlterReplicaLogDirsRequestData,
    LogDir,
    Topic,
)

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    int32Serializer,
    stringSerializer,
)


topicSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
}


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema)
    for version, schema in topicSchemas.items()
}


logDirSchemas: Dict[int, Schema] = {
    0: [
        ("log_dir", stringSerializer),
        ("topics", ArraySerializer(topicSerializers[0])),
    ],
    1: [
        ("log_dir", stringSerializer),
        ("topics", ArraySerializer(topicSerializers[1])),
    ],
}


logDirSerializers: Dict[int, DataClassSerializer[LogDir]] = {
    version: DataClassSerializer(LogDir, schema)
    for version, schema in logDirSchemas.items()
}


alterReplicaLogDirsRequestDataSchemas: Dict[int, Schema] = {
    0: [("log_dirs", ArraySerializer(logDirSerializers[0]))],
    1: [("log_dirs", ArraySerializer(logDirSerializers[1]))],
}


alterReplicaLogDirsRequestDataSerializers: Dict[
    int, DataClassSerializer[AlterReplicaLogDirsRequestData]
] = {
    version: DataClassSerializer(AlterReplicaLogDirsRequestData, schema)
    for version, schema in alterReplicaLogDirsRequestDataSchemas.items()
}
