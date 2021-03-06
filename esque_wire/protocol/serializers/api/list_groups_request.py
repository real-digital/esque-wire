###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.list_groups_request import ListGroupsRequestData
from ._main_serializers import ClassSerializer, Schema

listGroupsRequestDataSchemas: Dict[int, Schema] = {0: [], 1: [], 2: []}


listGroupsRequestDataSerializers: Dict[int, ClassSerializer[ListGroupsRequestData]] = {
    version: ClassSerializer(ListGroupsRequestData, schema) for version, schema in listGroupsRequestDataSchemas.items()
}

listGroupsRequestDataSerializers[-1] = listGroupsRequestDataSerializers[2]
