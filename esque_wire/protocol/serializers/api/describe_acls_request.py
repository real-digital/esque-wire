##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.describe_acls_request import DescribeAclsRequestData

from ._main_serializers import (
    ClassSerializer,
    DummySerializer,
    Schema,
    aclOperationSerializer,
    aclPermissionTypeSerializer,
    int8Serializer,
    nullableStringSerializer,
    resourceTypeSerializer,
)


describeAclsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ("resource_type", resourceTypeSerializer),
        ("resource_name", nullableStringSerializer),
        ("principal", nullableStringSerializer),
        ("host", nullableStringSerializer),
        ("operation", aclOperationSerializer),
        ("permission_type", aclPermissionTypeSerializer),
        ("resource_pattern_type_filter", DummySerializer(3)),
    ],
    1: [
        ("resource_type", resourceTypeSerializer),
        ("resource_name", nullableStringSerializer),
        ("resource_pattern_type_filter", int8Serializer),
        ("principal", nullableStringSerializer),
        ("host", nullableStringSerializer),
        ("operation", aclOperationSerializer),
        ("permission_type", aclPermissionTypeSerializer),
    ],
}


describeAclsRequestDataSerializers: Dict[int, ClassSerializer[DescribeAclsRequestData]] = {
    version: ClassSerializer(DescribeAclsRequestData, schema)
    for version, schema in describeAclsRequestDataSchemas.items()
}

describeAclsRequestDataSerializers[-1] = describeAclsRequestDataSerializers[1]
