##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.delete_groups_request import DeleteGroupsRequestData

from ._main_serializers import (
    ArraySerializer,
    DataClassSerializer,
    Schema,
    stringSerializer,
)


deleteGroupsRequestDataSchemas: Dict[int, Schema] = {
    0: [("groups", ArraySerializer(stringSerializer))],
    1: [("groups", ArraySerializer(stringSerializer))],
}


deleteGroupsRequestDataSerializers: Dict[
    int, DataClassSerializer[DeleteGroupsRequestData]
] = {
    version: DataClassSerializer(DeleteGroupsRequestData, schema)
    for version, schema in deleteGroupsRequestDataSchemas.items()
}
