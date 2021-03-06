###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.describe_log_dirs_response import DescribeLogDirsResponseData, LogDir, Partition, Topic
from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    booleanSerializer,
    errorCodeSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)

partitionSchemas: Dict[int, Schema] = {
    0: [
        ("partition", int32Serializer),
        ("size", int64Serializer),
        ("offset_lag", int64Serializer),
        ("is_future", booleanSerializer),
    ],
    1: [
        ("partition", int32Serializer),
        ("size", int64Serializer),
        ("offset_lag", int64Serializer),
        ("is_future", booleanSerializer),
    ],
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


logDirSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", errorCodeSerializer),
        ("log_dir", stringSerializer),
        ("topics", ArraySerializer(topicSerializers[0])),
    ],
    1: [
        ("error_code", errorCodeSerializer),
        ("log_dir", stringSerializer),
        ("topics", ArraySerializer(topicSerializers[1])),
    ],
}


logDirSerializers: Dict[int, ClassSerializer[LogDir]] = {
    version: ClassSerializer(LogDir, schema) for version, schema in logDirSchemas.items()
}

logDirSerializers[-1] = logDirSerializers[1]


describeLogDirsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("log_dirs", ArraySerializer(logDirSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("log_dirs", ArraySerializer(logDirSerializers[1]))],
}


describeLogDirsResponseDataSerializers: Dict[int, ClassSerializer[DescribeLogDirsResponseData]] = {
    version: ClassSerializer(DescribeLogDirsResponseData, schema)
    for version, schema in describeLogDirsResponseDataSchemas.items()
}

describeLogDirsResponseDataSerializers[-1] = describeLogDirsResponseDataSerializers[1]
