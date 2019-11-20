##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict

from ...structs.api.delete_groups_request import DeleteGroupsRequestData
from ._main_serializers import ArraySerializer, ClassSerializer, Schema, stringSerializer

deleteGroupsRequestDataSchemas: Dict[int, Schema] = {
    0: [("groups", ArraySerializer(stringSerializer))],
    1: [("groups", ArraySerializer(stringSerializer))],
}


deleteGroupsRequestDataSerializers: Dict[int, ClassSerializer[DeleteGroupsRequestData]] = {
    version: ClassSerializer(DeleteGroupsRequestData, schema)
    for version, schema in deleteGroupsRequestDataSchemas.items()
}

deleteGroupsRequestDataSerializers[-1] = deleteGroupsRequestDataSerializers[1]
