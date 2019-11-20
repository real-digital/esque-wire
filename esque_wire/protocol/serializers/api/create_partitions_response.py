##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.create_partitions_response import CreatePartitionsResponseData, TopicError

from ._main_serializers import (
    ArraySerializer,
    ClassSerializer,
    Schema,
    errorCodeSerializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


topicErrorSchemas: Dict[int, Schema] = {
    0: [("topic", stringSerializer), ("error_code", errorCodeSerializer), ("error_message", nullableStringSerializer)],
    1: [("topic", stringSerializer), ("error_code", errorCodeSerializer), ("error_message", nullableStringSerializer)],
}


topicErrorSerializers: Dict[int, ClassSerializer[TopicError]] = {
    version: ClassSerializer(TopicError, schema) for version, schema in topicErrorSchemas.items()
}

topicErrorSerializers[-1] = topicErrorSerializers[1]


createPartitionsResponseDataSchemas: Dict[int, Schema] = {
    0: [("throttle_time_ms", int32Serializer), ("topic_errors", ArraySerializer(topicErrorSerializers[0]))],
    1: [("throttle_time_ms", int32Serializer), ("topic_errors", ArraySerializer(topicErrorSerializers[1]))],
}


createPartitionsResponseDataSerializers: Dict[int, ClassSerializer[CreatePartitionsResponseData]] = {
    version: ClassSerializer(CreatePartitionsResponseData, schema)
    for version, schema in createPartitionsResponseDataSchemas.items()
}

createPartitionsResponseDataSerializers[-1] = createPartitionsResponseDataSerializers[1]
