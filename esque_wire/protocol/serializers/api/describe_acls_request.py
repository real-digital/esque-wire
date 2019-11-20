##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.describe_acls_request import DescribeAclsRequestData

from esque_wire.protocol.serializers import (
    DataClassSerializer,
    DummySerializer,
    Schema,
    int8Serializer,
    nullableStringSerializer,
)


describeAclsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("resource_type", int8Serializer),
        ("resource_name", nullableStringSerializer),
        ("principal", nullableStringSerializer),
        ("host", nullableStringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
        ("resource_pattern_type_filter", DummySerializer(3)),
    ],
    1: [
        ("resource_type", int8Serializer),
        ("resource_name", nullableStringSerializer),
        ("resource_pattern_type_filter", int8Serializer),
        ("principal", nullableStringSerializer),
        ("host", nullableStringSerializer),
        ("operation", int8Serializer),
        ("permission_type", int8Serializer),
    ],
}


describeAclsRequestDataSerializers: Dict[
    int, DataClassSerializer[DescribeAclsRequestData]
] = {
    version: DataClassSerializer(DescribeAclsRequestData, schema)
    for version, schema in describeAclsRequestDataSchemas.items()
}