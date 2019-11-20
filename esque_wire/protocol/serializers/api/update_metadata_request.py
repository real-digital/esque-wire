##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.update_metadata_request import (
    EndPoint,
    LiveBroker,
    PartitionState,
    TopicState,
    UpdateMetadataRequestData,
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


endPointSchemas: Dict[int, Schema] = {
    1: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("security_protocol_type", int16Serializer),
        ("listener_name", DummySerializer(stringSerializer.default)),
    ],
    2: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("security_protocol_type", int16Serializer),
        ("listener_name", DummySerializer(stringSerializer.default)),
    ],
    3: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("listener_name", stringSerializer),
        ("security_protocol_type", int16Serializer),
    ],
    4: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("listener_name", stringSerializer),
        ("security_protocol_type", int16Serializer),
    ],
    5: [
        ("port", int32Serializer),
        ("host", stringSerializer),
        ("listener_name", stringSerializer),
        ("security_protocol_type", int16Serializer),
    ],
}


endPointSerializers: Dict[int, DataClassSerializer[EndPoint]] = {
    version: DataClassSerializer(EndPoint, schema)
    for version, schema in endPointSchemas.items()
}


liveBrokerSchemas: Dict[int, Schema] = {
    0: [
        ("id", int32Serializer),
        (None, stringSerializer),
        (None, int32Serializer),
        (
            "end_points",
            DummySerializer(ArraySerializer(endPointSerializers[0]).default),
        ),
        ("rack", DummySerializer(nullableStringSerializer.default)),
    ],
    1: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointSerializers[1])),
        ("rack", DummySerializer(nullableStringSerializer.default)),
    ],
    2: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointSerializers[2])),
        ("rack", nullableStringSerializer),
    ],
    3: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointSerializers[3])),
        ("rack", nullableStringSerializer),
    ],
    4: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointSerializers[4])),
        ("rack", nullableStringSerializer),
    ],
    5: [
        ("id", int32Serializer),
        ("end_points", ArraySerializer(endPointSerializers[5])),
        ("rack", nullableStringSerializer),
    ],
}


liveBrokerSerializers: Dict[int, DataClassSerializer[LiveBroker]] = {
    version: DataClassSerializer(LiveBroker, schema)
    for version, schema in liveBrokerSchemas.items()
}


partitionStateSchemas: Dict[int, Schema] = {
    0: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer(ArraySerializer(int32Serializer).default)),
    ],
    1: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer(ArraySerializer(int32Serializer).default)),
    ],
    2: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer(ArraySerializer(int32Serializer).default)),
    ],
    3: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", DummySerializer(ArraySerializer(int32Serializer).default)),
    ],
    4: [
        (None, stringSerializer),
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
    ],
    5: [
        ("partition", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("leader", int32Serializer),
        ("leader_epoch", int32Serializer),
        ("isr", ArraySerializer(int32Serializer)),
        ("zk_version", int32Serializer),
        ("replicas", ArraySerializer(int32Serializer)),
        ("offline_replicas", ArraySerializer(int32Serializer)),
    ],
}


partitionStateSerializers: Dict[int, DataClassSerializer[PartitionState]] = {
    version: DataClassSerializer(PartitionState, schema)
    for version, schema in partitionStateSchemas.items()
}


topicStateSchemas: Dict[int, Schema] = {
    5: [
        ("topic", stringSerializer),
        ("partition_states", ArraySerializer(partitionStateSerializers[5])),
    ]
}


topicStateSerializers: Dict[int, DataClassSerializer[TopicState]] = {
    version: DataClassSerializer(TopicState, schema)
    for version, schema in topicStateSchemas.items()
}


updateMetadataRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[0])),
        ("live_brokers", ArraySerializer(liveBrokerSerializers[0])),
        ("broker_epoch", DummySerializer(int64Serializer.default)),
        (
            "topic_states",
            DummySerializer(ArraySerializer(topicStateSerializers[0]).default),
        ),
    ],
    1: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[1])),
        ("live_brokers", ArraySerializer(liveBrokerSerializers[1])),
        ("broker_epoch", DummySerializer(int64Serializer.default)),
        (
            "topic_states",
            DummySerializer(ArraySerializer(topicStateSerializers[0]).default),
        ),
    ],
    2: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[2])),
        ("live_brokers", ArraySerializer(liveBrokerSerializers[2])),
        ("broker_epoch", DummySerializer(int64Serializer.default)),
        (
            "topic_states",
            DummySerializer(ArraySerializer(topicStateSerializers[0]).default),
        ),
    ],
    3: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[3])),
        ("live_brokers", ArraySerializer(liveBrokerSerializers[3])),
        ("broker_epoch", DummySerializer(int64Serializer.default)),
        (
            "topic_states",
            DummySerializer(ArraySerializer(topicStateSerializers[0]).default),
        ),
    ],
    4: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[4])),
        ("live_brokers", ArraySerializer(liveBrokerSerializers[4])),
        ("broker_epoch", DummySerializer(int64Serializer.default)),
        (
            "topic_states",
            DummySerializer(ArraySerializer(topicStateSerializers[0]).default),
        ),
    ],
    5: [
        ("controller_id", int32Serializer),
        ("controller_epoch", int32Serializer),
        ("broker_epoch", int64Serializer),
        ("topic_states", ArraySerializer(topicStateSerializers[5])),
        ("live_brokers", ArraySerializer(liveBrokerSerializers[5])),
    ],
}


updateMetadataRequestDataSerializers: Dict[
    int, DataClassSerializer[UpdateMetadataRequestData]
] = {
    version: DataClassSerializer(UpdateMetadataRequestData, schema)
    for version, schema in updateMetadataRequestDataSchemas.items()
}
