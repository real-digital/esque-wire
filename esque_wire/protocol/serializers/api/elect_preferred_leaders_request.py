##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.elect_preferred_leaders_request import ElectPreferredLeadersRequestData, TopicPartition
from ._main_serializers import ArraySerializer, ClassSerializer, Schema, int32Serializer, stringSerializer

topicPartitionSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("partition_id", ArraySerializer(int32Serializer))]
}


topicPartitionSerializers: Dict[int, ClassSerializer[TopicPartition]] = {
    version: ClassSerializer(TopicPartition, schema) for version, schema in topicPartitionSchemas.items()
}

topicPartitionSerializers[-1] = topicPartitionSerializers[0]


electPreferredLeadersRequestDataSchemas: Dict[int, Schema] = {
    0: [("topic_partitions", ArraySerializer(topicPartitionSerializers[0])), ("timeout_ms", int32Serializer)]
}


electPreferredLeadersRequestDataSerializers: Dict[int, ClassSerializer[ElectPreferredLeadersRequestData]] = {
    version: ClassSerializer(ElectPreferredLeadersRequestData, schema)
    for version, schema in electPreferredLeadersRequestDataSchemas.items()
}

electPreferredLeadersRequestDataSerializers[-1] = electPreferredLeadersRequestDataSerializers[0]
