##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.describe_log_dirs_response import (
    DescribeLogDirsResponseData,
    LogDir,
    Partition,
    Topic,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    booleanSerializer,
    int16Serializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)


partitionSchemas: Dict[int, Schema] = {
    0: [
        ('partition', int32Serializer),
        ('size', int64Serializer),
        ('offset_lag', int64Serializer),
        ('is_future', booleanSerializer),
    ],
    1: [
        ('partition', int32Serializer),
        ('size', int64Serializer),
        ('offset_lag', int64Serializer),
        ('is_future', booleanSerializer),
    ],
}


partitionSerializers: Dict[int, DataClassSerializer[Partition]] = {
    version: DataClassSerializer(Partition, schema) for version, schema
    in partitionSchemas.items()
}


topicSchemas: Dict[int, Schema] = {
    0: [
        ('topic', stringSerializer),
        ('partitions', ArraySerializer(partitionSerializers[0])),
    ],
    1: [
        ('topic', stringSerializer),
        ('partitions', ArraySerializer(partitionSerializers[1])),
    ],
}


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema) for version, schema
    in topicSchemas.items()
}


logDirSchemas: Dict[int, Schema] = {
    0: [
        ('error_code', int16Serializer),
        ('log_dir', stringSerializer),
        ('topics', ArraySerializer(topicSerializers[0])),
    ],
    1: [
        ('error_code', int16Serializer),
        ('log_dir', stringSerializer),
        ('topics', ArraySerializer(topicSerializers[1])),
    ],
}


logDirSerializers: Dict[int, DataClassSerializer[LogDir]] = {
    version: DataClassSerializer(LogDir, schema) for version, schema
    in logDirSchemas.items()
}


describeLogDirsResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ('throttle_time_ms', int32Serializer),
        ('log_dirs', ArraySerializer(logDirSerializers[0])),
    ],
    1: [
        ('throttle_time_ms', int32Serializer),
        ('log_dirs', ArraySerializer(logDirSerializers[1])),
    ],
}


describeLogDirsResponseDataSerializers: Dict[int, DataClassSerializer[DescribeLogDirsResponseData]] = {
    version: DataClassSerializer(DescribeLogDirsResponseData, schema) for version, schema
    in describeLogDirsResponseDataSchemas.items()
}

