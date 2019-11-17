##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from esque_wire.protocol.structs.alter_configs_request import (
    AlterConfigsRequestData,
    ConfigEntry,
    Resource,
)

from esque_wire.protocol.serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    booleanSerializer,
    int8Serializer,
    nullableStringSerializer,
    stringSerializer,
)


configEntrySchemas: Dict[int, Schema] = {
    0: [
        ('config_name', stringSerializer),
        ('config_value', nullableStringSerializer),
    ],
    1: [
        ('config_name', stringSerializer),
        ('config_value', nullableStringSerializer),
    ],
}


configEntrySerializers: Dict[int, DataClassSerializer[ConfigEntry]] = {
    version: DataClassSerializer(ConfigEntry, schema) for version, schema
    in configEntrySchemas.items()
}


resourceSchemas: Dict[int, Schema] = {
    0: [
        ('resource_type', int8Serializer),
        ('resource_name', stringSerializer),
        ('config_entries', ArraySerializer(configEntrySerializers[0])),
    ],
    1: [
        ('resource_type', int8Serializer),
        ('resource_name', stringSerializer),
        ('config_entries', ArraySerializer(configEntrySerializers[1])),
    ],
}


resourceSerializers: Dict[int, DataClassSerializer[Resource]] = {
    version: DataClassSerializer(Resource, schema) for version, schema
    in resourceSchemas.items()
}


alterConfigsRequestDataSchemas: Dict[int, Schema] = {
    0: [
        ('resources', ArraySerializer(resourceSerializers[0])),
        ('validate_only', booleanSerializer),
    ],
    1: [
        ('resources', ArraySerializer(resourceSerializers[1])),
        ('validate_only', booleanSerializer),
    ],
}


alterConfigsRequestDataSerializers: Dict[int, DataClassSerializer[AlterConfigsRequestData]] = {
    version: DataClassSerializer(AlterConfigsRequestData, schema) for version, schema
    in alterConfigsRequestDataSchemas.items()
}

