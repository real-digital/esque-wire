##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.fetch_request import FetchRequestData, ForgottenTopicsData, Partition, Topic

from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    DummySerializer,
    Schema,
    int32Serializer,
    int64Serializer,
    int8Serializer,
    stringSerializer,
)


forgottenTopicsDataSchemas: Dict[int, Schema] = {
    7: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    8: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    9: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    10: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
    11: [("topic", stringSerializer), ("partitions", ArraySerializer(int32Serializer))],
}


forgottenTopicsDataSerializers: Dict[int, ClassSerializer[ForgottenTopicsData]] = {
    version: ClassSerializer(ForgottenTopicsData, schema) for version, schema in forgottenTopicsDataSchemas.items()
}

forgottenTopicsDataSerializers[-1] = forgottenTopicsDataSerializers[11]


partitionSchemas: Dict[int, Schema] = {
    0: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
        ("log_start_offset", DummySerializer(int64Serializer.default)),
    ],
    1: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
        ("log_start_offset", DummySerializer(int64Serializer.default)),
    ],
    2: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
        ("log_start_offset", DummySerializer(int64Serializer.default)),
    ],
    3: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
        ("log_start_offset", DummySerializer(int64Serializer.default)),
    ],
    4: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
        ("log_start_offset", DummySerializer(int64Serializer.default)),
    ],
    5: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    6: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    7: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    8: [
        ("partition", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
        ("current_leader_epoch", DummySerializer(int32Serializer.default)),
    ],
    9: [
        ("partition", int32Serializer),
        ("current_leader_epoch", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
    ],
    10: [
        ("partition", int32Serializer),
        ("current_leader_epoch", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
    ],
    11: [
        ("partition", int32Serializer),
        ("current_leader_epoch", int32Serializer),
        ("fetch_offset", int64Serializer),
        ("log_start_offset", int64Serializer),
        ("partition_max_bytes", int32Serializer),
    ],
}


partitionSerializers: Dict[int, ClassSerializer[Partition]] = {
    version: ClassSerializer(Partition, schema) for version, schema in partitionSchemas.items()
}

partitionSerializers[-1] = partitionSerializers[11]


topicSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[0]))],
    1: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[1]))],
    2: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[2]))],
    3: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[3]))],
    4: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[4]))],
    5: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[5]))],
    6: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[6]))],
    7: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[7]))],
    8: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[8]))],
    9: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[9]))],
    10: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[10]))],
    11: [("topic", stringSerializer), ("partitions", ArraySerializer(partitionSerializers[11]))],
}


topicSerializers: Dict[int, ClassSerializer[Topic]] = {
    version: ClassSerializer(Topic, schema) for version, schema in topicSchemas.items()
}

topicSerializers[-1] = topicSerializers[11]


fetchRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[0])),
        ("max_bytes", DummySerializer(int32Serializer.default)),
        ("isolation_level", DummySerializer(int8Serializer.default)),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    1: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[1])),
        ("max_bytes", DummySerializer(int32Serializer.default)),
        ("isolation_level", DummySerializer(int8Serializer.default)),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    2: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[2])),
        ("max_bytes", DummySerializer(int32Serializer.default)),
        ("isolation_level", DummySerializer(int8Serializer.default)),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    3: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[3])),
        ("isolation_level", DummySerializer(int8Serializer.default)),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    4: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[4])),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    5: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[5])),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    6: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("topics", ArraySerializer(topicSerializers[6])),
        ("session_id", DummySerializer(int32Serializer.default)),
        ("session_epoch", DummySerializer(int32Serializer.default)),
        ("forgotten_topics_data", DummySerializer(ArraySerializer(forgottenTopicsDataSerializers[-1]).default)),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    7: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("session_id", int32Serializer),
        ("session_epoch", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[7])),
        ("forgotten_topics_data", ArraySerializer(forgottenTopicsDataSerializers[7])),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    8: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("session_id", int32Serializer),
        ("session_epoch", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[8])),
        ("forgotten_topics_data", ArraySerializer(forgottenTopicsDataSerializers[8])),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    9: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("session_id", int32Serializer),
        ("session_epoch", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[9])),
        ("forgotten_topics_data", ArraySerializer(forgottenTopicsDataSerializers[9])),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    10: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("session_id", int32Serializer),
        ("session_epoch", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[10])),
        ("forgotten_topics_data", ArraySerializer(forgottenTopicsDataSerializers[10])),
        ("rack_id", DummySerializer(stringSerializer.default)),
    ],
    11: [
        ("replica_id", int32Serializer),
        ("max_wait_time", int32Serializer),
        ("min_bytes", int32Serializer),
        ("max_bytes", int32Serializer),
        ("isolation_level", int8Serializer),
        ("session_id", int32Serializer),
        ("session_epoch", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[11])),
        ("forgotten_topics_data", ArraySerializer(forgottenTopicsDataSerializers[11])),
        ("rack_id", stringSerializer),
    ],
}


fetchRequestDataSerializers: Dict[int, ClassSerializer[FetchRequestData]] = {
    version: ClassSerializer(FetchRequestData, schema) for version, schema in fetchRequestDataSchemas.items()
}

fetchRequestDataSerializers[-1] = fetchRequestDataSerializers[11]
