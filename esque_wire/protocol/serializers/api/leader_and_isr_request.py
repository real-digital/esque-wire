##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.leader_and_isr_request import (
    LeaderAndIsrRequestData,
    LiveLeader,
    PartitionState,
    TopicState,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    booleanSerializer,
    int32Serializer,
    int64Serializer,
    stringSerializer,
)


liveLeaderSchemas: Dict[int, Schema] = {
    0: [
        ('id', int32Serializer),
        ('host', stringSerializer),
        ('port', int32Serializer),
    ],
    1: [
        ('id', int32Serializer),
        ('host', stringSerializer),
        ('port', int32Serializer),
    ],
    2: [
        ('id', int32Serializer),
        ('host', stringSerializer),
        ('port', int32Serializer),
    ],
}


liveLeaderSerializers: Dict[int, DataClassSerializer[LiveLeader]] = {
    version: DataClassSerializer(LiveLeader, schema) for version, schema
    in liveLeaderSchemas.items()
}


partitionStateSchemas: Dict[int, Schema] = {
    0: [
        (None, stringSerializer),
        ('partition', int32Serializer),
        ('controller_epoch', int32Serializer),
        ('leader', int32Serializer),
        ('leader_epoch', int32Serializer),
        ('isr', ArraySerializer(int32Serializer)),
        ('zk_version', int32Serializer),
        ('replicas', ArraySerializer(int32Serializer)),
        ('is_new', DummySerializer(booleanSerializer.default)),
    ],
    1: [
        (None, stringSerializer),
        ('partition', int32Serializer),
        ('controller_epoch', int32Serializer),
        ('leader', int32Serializer),
        ('leader_epoch', int32Serializer),
        ('isr', ArraySerializer(int32Serializer)),
        ('zk_version', int32Serializer),
        ('replicas', ArraySerializer(int32Serializer)),
        ('is_new', booleanSerializer),
    ],
    2: [
        ('partition', int32Serializer),
        ('controller_epoch', int32Serializer),
        ('leader', int32Serializer),
        ('leader_epoch', int32Serializer),
        ('isr', ArraySerializer(int32Serializer)),
        ('zk_version', int32Serializer),
        ('replicas', ArraySerializer(int32Serializer)),
        ('is_new', booleanSerializer),
    ],
}


partitionStateSerializers: Dict[int, DataClassSerializer[PartitionState]] = {
    version: DataClassSerializer(PartitionState, schema) for version, schema
    in partitionStateSchemas.items()
}


topicStateSchemas: Dict[int, Schema] = {
    2: [
        ('topic', stringSerializer),
        ('partition_states', ArraySerializer(partitionStateSerializers[2])),
    ],
}


topicStateSerializers: Dict[int, DataClassSerializer[TopicState]] = {
    version: DataClassSerializer(TopicState, schema) for version, schema
    in topicStateSchemas.items()
}


leaderAndIsrRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ('controller_id', int32Serializer),
        ('controller_epoch', int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[0])),
        ('live_leaders', ArraySerializer(liveLeaderSerializers[0])),
        ('broker_epoch', DummySerializer(int64Serializer.default)),
        ('topic_states', DummySerializer(ArraySerializer(topicStateSerializers[0]).default)),
    ],
    1: [
        ('controller_id', int32Serializer),
        ('controller_epoch', int32Serializer),
        (None, ArraySerializer(partitionStateSerializers[1])),
        ('live_leaders', ArraySerializer(liveLeaderSerializers[1])),
        ('broker_epoch', DummySerializer(int64Serializer.default)),
        ('topic_states', DummySerializer(ArraySerializer(topicStateSerializers[0]).default)),
    ],
    2: [
        ('controller_id', int32Serializer),
        ('controller_epoch', int32Serializer),
        ('broker_epoch', int64Serializer),
        ('topic_states', ArraySerializer(topicStateSerializers[2])),
        ('live_leaders', ArraySerializer(liveLeaderSerializers[2])),
    ],
}


leaderAndIsrRequestDataSerializers: Dict[int, DataClassSerializer[LeaderAndIsrRequestData]] = {
    version: DataClassSerializer(LeaderAndIsrRequestData, schema) for version, schema
    in leaderAndIsrRequestDataSchemas.items()
}

