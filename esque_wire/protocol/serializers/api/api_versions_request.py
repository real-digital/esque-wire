##############################################
# Autogenerated module. Please don't modify. #
##############################################

from typing import Dict
from ...structs.api.api_versions_request import ApiVersionsRequestData

from ._main_serializers import DataClassSerializer, Schema


apiVersionsRequestDataSchemas: Dict[int, Schema] = {0: [], 1: [], 2: []}


apiVersionsRequestDataSerializers: Dict[
    int, DataClassSerializer[ApiVersionsRequestData]
] = {
    version: DataClassSerializer(ApiVersionsRequestData, schema)
    for version, schema in apiVersionsRequestDataSchemas.items()
}
