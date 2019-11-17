##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.delete_acls_request import (
    DeleteAclsRequestData,
    Filter,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    DummySerializer,
    Schema,
    int8Serializer,
    nullableStringSerializer,
)


filterSchemas: Dict[int, Schema] = {
    0: [
        ('resource_type', int8Serializer),
        ('resource_name', nullableStringSerializer),
        ('principal', nullableStringSerializer),
        ('host', nullableStringSerializer),
        ('operation', int8Serializer),
        ('permission_type', int8Serializer),
        ('resource_pattern_type_filter', DummySerializer(3)),
    ],
    1: [
        ('resource_type', int8Serializer),
        ('resource_name', nullableStringSerializer),
        ('resource_pattern_type_filter', int8Serializer),
        ('principal', nullableStringSerializer),
        ('host', nullableStringSerializer),
        ('operation', int8Serializer),
        ('permission_type', int8Serializer),
    ],
}


filterSerializers: Dict[int, DataClassSerializer[Filter]] = {
    version: DataClassSerializer(Filter, schema) for version, schema
    in filterSchemas.items()
}


deleteAclsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ('filters', ArraySerializer(filterSerializers[0])),
    ],
    1: [
        ('filters', ArraySerializer(filterSerializers[1])),
    ],
}


deleteAclsRequestDataSerializers: Dict[int, DataClassSerializer[DeleteAclsRequestData]] = {
    version: DataClassSerializer(DeleteAclsRequestData, schema) for version, schema
    in deleteAclsRequestDataSchemas.items()
}

