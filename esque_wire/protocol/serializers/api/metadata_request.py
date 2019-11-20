##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.metadata_request import MetadataRequestData, Topic

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    booleanSerializer,
    stringSerializer,
)


topicSchemas: Dict[int, Schema] = {
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


topicSerializers: Dict[int, DataClassSerializer[Topic]] = {
    version: DataClassSerializer(Topic, schema)
    for version, schema in topicSchemas.items()
}


metadataRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("topics", ArraySerializer(topicSerializers[0])),
        ("allow_auto_topic_creation", DummySerializer(booleanSerializer.default)),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    1: [
        ("topics", ArraySerializer(topicSerializers[1])),
        ("allow_auto_topic_creation", DummySerializer(booleanSerializer.default)),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    2: [
        ("topics", ArraySerializer(topicSerializers[2])),
        ("allow_auto_topic_creation", DummySerializer(booleanSerializer.default)),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    3: [
        ("topics", ArraySerializer(topicSerializers[3])),
        ("allow_auto_topic_creation", DummySerializer(booleanSerializer.default)),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    4: [
        ("topics", ArraySerializer(topicSerializers[4])),
        ("allow_auto_topic_creation", booleanSerializer),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    5: [
        ("topics", ArraySerializer(topicSerializers[5])),
        ("allow_auto_topic_creation", booleanSerializer),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    6: [
        ("topics", ArraySerializer(topicSerializers[6])),
        ("allow_auto_topic_creation", booleanSerializer),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    7: [
        ("topics", ArraySerializer(topicSerializers[7])),
        ("allow_auto_topic_creation", booleanSerializer),
        (
            "include_cluster_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
        (
            "include_topic_authorized_operations",
            DummySerializer(booleanSerializer.default),
        ),
    ],
    8: [
        ("topics", ArraySerializer(topicSerializers[8])),
        ("allow_auto_topic_creation", booleanSerializer),
        ("include_cluster_authorized_operations", booleanSerializer),
        ("include_topic_authorized_operations", booleanSerializer),
    ],
}


metadataRequestDataSerializers: Dict[int, DataClassSerializer[MetadataRequestData]] = {
    version: DataClassSerializer(MetadataRequestData, schema)
    for version, schema in metadataRequestDataSchemas.items()
}
