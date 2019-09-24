from typing import Dict, List, Optional

from dataclasses import dataclass

from esque_wire.protocol.api.base import ApiKey, RequestData, ResponseData
from esque_wire.protocol.serializers import (
    ArraySerializer,
    BaseSerializer,
    DummySerializer,
    NamedTupleSerializer,
    Schema,
    booleanSerializer,
    int16Serializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


@dataclass
class RequestedTopic:
    # The topic name.
    name: "str"  # STRING


@dataclass
class MetadataRequestData(RequestData):
    # The topics to fetch metadata for.
    # None to fetch all topics
    # Empty list to fetch no topics
    # If version is 0: None is not supported (?), and empty list fetches all topics
    topics: Optional[List["RequestedTopic"]]

    # If this is true, the broker may auto-create topics that we requested which do not already exist, if
    # it is configured to do so.
    allow_auto_topic_creation: "bool"  # BOOLEAN

    # Whether to include cluster authorized operations.
    include_cluster_authorized_operations: "bool"  # BOOLEAN

    # Whether to include topic authorized operations.
    include_topic_authorized_operations: "bool"  # BOOLEAN

    @staticmethod
    def api_key() -> int:
        return ApiKey.METADATA  # == 3


@dataclass
class Broker:
    # The broker ID.
    node_id: "int"  # INT32

    # The broker hostname.
    host: "str"  # STRING

    # The broker port.
    port: "int"  # INT32

    # The rack of the broker, or null if it has not been assigned to a rack.
    rack: "Optional[str]"  # NULLABLE_STRING


@dataclass
class Partition:
    # The partition error, or 0 if there was no error.
    error_code: "int"  # INT16

    # The partition index.
    partition_index: "int"  # INT32

    # The ID of the leader broker.
    leader_id: "int"  # INT32

    # The leader epoch of this partition.
    leader_epoch: "int"  # INT32

    # The set of all nodes that host this partition.
    replica_nodes: List["int"]  # INT32

    # The set of nodes that are in sync with the leader for this partition.
    isr_nodes: List["int"]  # INT32

    # The set of offline replicas of this partition.
    offline_replicas: List["int"]  # INT32


@dataclass
class Topic:
    # The partition error, or 0 if there was no error.
    error_code: "int"  # INT16

    # The topic name.
    name: "str"  # STRING

    # True if the topic is internal.
    is_internal: "bool"  # BOOLEAN

    # Each partition in the topic.
    partitions: List["Partition"]

    # 32-bit bitfield to represent authorized operations for this topic.
    topic_authorized_operations: "int"  # INT32


@dataclass
class MetadataResponseData(ResponseData):
    # The duration in milliseconds for which the request was throttled due to a quota violation, or zero
    # if the request did not violate any quota.
    throttle_time_ms: "int"  # INT32

    # Each broker in the response.
    brokers: List["Broker"]

    # The cluster ID that responding broker belongs to.
    cluster_id: "Optional[str]"  # NULLABLE_STRING

    # The ID of the controller broker.
    controller_id: "int"  # INT32

    # Each topic in the response.
    topics: List["Topic"]

    # 32-bit bitfield to represent authorized operations for this cluster.
    cluster_authorized_operations: "int"  # INT32

    @staticmethod
    def api_key() -> int:
        return ApiKey.METADATA  # == 3


requestedTopicSchemas: Dict[int, Schema] = {
    0: [("name", stringSerializer)],
    1: [("name", stringSerializer)],
    2: [("name", stringSerializer)],
    3: [("name", stringSerializer)],
    4: [("name", stringSerializer)],
    5: [("name", stringSerializer)],
    6: [("name", stringSerializer)],
    7: [("name", stringSerializer)],
    8: [("name", stringSerializer)],
}


requestedTopicSerializers: Dict[int, BaseSerializer[RequestedTopic]] = {
    version: NamedTupleSerializer(RequestedTopic, schema) for version, schema in requestedTopicSchemas.items()
}


metadataRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("topics", ArraySerializer(requestedTopicSerializers[0])),
        ("allow_auto_topic_creation", DummySerializer(bool())),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    1: [
        ("topics", ArraySerializer(requestedTopicSerializers[1])),
        ("allow_auto_topic_creation", DummySerializer(bool())),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    2: [
        ("topics", ArraySerializer(requestedTopicSerializers[2])),
        ("allow_auto_topic_creation", DummySerializer(bool())),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    3: [
        ("topics", ArraySerializer(requestedTopicSerializers[3])),
        ("allow_auto_topic_creation", DummySerializer(bool())),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    4: [
        ("topics", ArraySerializer(requestedTopicSerializers[4])),
        ("allow_auto_topic_creation", booleanSerializer),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    5: [
        ("topics", ArraySerializer(requestedTopicSerializers[5])),
        ("allow_auto_topic_creation", booleanSerializer),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    6: [
        ("topics", ArraySerializer(requestedTopicSerializers[6])),
        ("allow_auto_topic_creation", booleanSerializer),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    7: [
        ("topics", ArraySerializer(requestedTopicSerializers[7])),
        ("allow_auto_topic_creation", booleanSerializer),
        ("include_cluster_authorized_operations", DummySerializer(bool())),
        ("include_topic_authorized_operations", DummySerializer(bool())),
    ],
    8: [
        ("topics", ArraySerializer(requestedTopicSerializers[8])),
        ("allow_auto_topic_creation", booleanSerializer),
        ("include_cluster_authorized_operations", booleanSerializer),
        ("include_topic_authorized_operations", booleanSerializer),
    ],
}


metadataRequestDataSerializers: Dict[int, BaseSerializer[MetadataRequestData]] = {
    version: NamedTupleSerializer(MetadataRequestData, schema)
    for version, schema in metadataRequestDataSchemas.items()
}


brokerSchemas: Dict[int, Schema] = {
    0: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", DummySerializer(None)),
    ],
    1: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    2: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    3: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    4: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    5: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    6: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    7: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
    8: [
        ("node_id", int32Serializer),
        ("host", stringSerializer),
        ("port", int32Serializer),
        ("rack", nullableStringSerializer),
    ],
}


brokerSerializers: Dict[int, BaseSerializer[Broker]] = {
    version: NamedTupleSerializer(Broker, schema) for version, schema in brokerSchemas.items()
}


partitionSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
        ("offline_replicas", DummySerializer([])),
    ],
    1: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
        ("offline_replicas", DummySerializer([])),
    ],
    2: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
        ("offline_replicas", DummySerializer([])),
    ],
    3: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
        ("offline_replicas", DummySerializer([])),
    ],
    4: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
        ("offline_replicas", DummySerializer([])),
    ],
    5: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
    ],
    6: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
        ("leader_epoch", DummySerializer(int())),
    ],
    7: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
    ],
    8: [
        ("error_code", int16Serializer),
        ("partition_index", int32Serializer),
        ("leader_id", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("replica_nodes", ArraySerializer(int32Serializer)),
        ("isr_nodes", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
    ],
}


partitionSerializers: Dict[int, BaseSerializer[Partition]] = {
    version: NamedTupleSerializer(Partition, schema) for version, schema in partitionSchemas.items()
}


topicSchemas: Dict[int, Schema] = {
    0: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("partitions", ArraySerializer(partitionSerializers[0])),
        ("is_internal", DummySerializer(bool())),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    1: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[1])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    2: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[2])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    3: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[3])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    4: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[4])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    5: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[5])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    6: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[6])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    7: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[7])),
        ("topic_authorized_operations", DummySerializer(int())),
    ],
    8: [
        ("error_code", int16Serializer),
        ("name", stringSerializer),
        ("is_internal", booleanSerializer),
        ("partitions", ArraySerializer(partitionSerializers[8])),
        ("topic_authorized_operations", int32Serializer),
    ],
}


topicSerializers: Dict[int, BaseSerializer[Topic]] = {
    version: NamedTupleSerializer(Topic, schema) for version, schema in topicSchemas.items()
}


metadataResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("brokers", ArraySerializer(brokerSerializers[0])),
        ("topics", ArraySerializer(topicSerializers[0])),
        ("throttle_time_ms", DummySerializer(int())),
        ("cluster_id", DummySerializer(None)),
        ("controller_id", DummySerializer(int())),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    1: [
        ("brokers", ArraySerializer(brokerSerializers[1])),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[1])),
        ("throttle_time_ms", DummySerializer(int())),
        ("cluster_id", DummySerializer(None)),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    2: [
        ("brokers", ArraySerializer(brokerSerializers[2])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[2])),
        ("throttle_time_ms", DummySerializer(int())),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    3: [
        ("throttle_time_ms", int32Serializer),
        ("brokers", ArraySerializer(brokerSerializers[3])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[3])),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    4: [
        ("throttle_time_ms", int32Serializer),
        ("brokers", ArraySerializer(brokerSerializers[4])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[4])),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    5: [
        ("throttle_time_ms", int32Serializer),
        ("brokers", ArraySerializer(brokerSerializers[5])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[5])),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    6: [
        ("throttle_time_ms", int32Serializer),
        ("brokers", ArraySerializer(brokerSerializers[6])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[6])),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    7: [
        ("throttle_time_ms", int32Serializer),
        ("brokers", ArraySerializer(brokerSerializers[7])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[7])),
        ("cluster_authorized_operations", DummySerializer(int())),
    ],
    8: [
        ("throttle_time_ms", int32Serializer),
        ("brokers", ArraySerializer(brokerSerializers[8])),
        ("cluster_id", nullableStringSerializer),
        ("controller_id", int32Serializer),
        ("topics", ArraySerializer(topicSerializers[8])),
        ("cluster_authorized_operations", int32Serializer),
    ],
}


metadataResponseDataSerializers: Dict[int, BaseSerializer[MetadataResponseData]] = {
    version: NamedTupleSerializer(MetadataResponseData, schema)
    for version, schema in metadataResponseDataSchemas.items()
}
