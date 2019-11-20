##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.create_partitions_response import (
    CreatePartitionsResponseData,
    TopicError,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    int16Serializer,
    int32Serializer,
    nullableStringSerializer,
    stringSerializer,
)


topicErrorSchemas: Dict[int, Schema] = {
    0: [
        ("topic", stringSerializer),
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
    ],
    1: [
        ("topic", stringSerializer),
        ("error_code", int16Serializer),
        ("error_message", nullableStringSerializer),
    ],
}


topicErrorSerializers: Dict[int, DataClassSerializer[TopicError]] = {
    version: DataClassSerializer(TopicError, schema)
    for version, schema in topicErrorSchemas.items()
}


createPartitionsResponseDataSchemas: Dict[int, Schema] = {
    0: [
        ("throttle_time_ms", int32Serializer),
        ("topic_errors", ArraySerializer(topicErrorSerializers[0])),
    ],
    1: [
        ("throttle_time_ms", int32Serializer),
        ("topic_errors", ArraySerializer(topicErrorSerializers[1])),
    ],
}


createPartitionsResponseDataSerializers: Dict[
    int, DataClassSerializer[CreatePartitionsResponseData]
] = {
    version: DataClassSerializer(CreatePartitionsResponseData, schema)
    for version, schema in createPartitionsResponseDataSchemas.items()
}