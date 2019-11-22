###############################################################
# Autogenerated module. Please don't modify.                  #
# Edit according file in protocol_generator/templates instead #
###############################################################

from typing import Dict

from ...structs.api.update_metadata_response import UpdateMetadataResponseData
from ._main_serializers import ClassSerializer, Schema, errorCodeSerializer

updateMetadataResponseDataSchemas: Dict[int, Schema] = {
    0: [("error_code", errorCodeSerializer)],
    1: [("error_code", errorCodeSerializer)],
    2: [("error_code", errorCodeSerializer)],
    3: [("error_code", errorCodeSerializer)],
    4: [("error_code", errorCodeSerializer)],
    5: [("error_code", errorCodeSerializer)],
}


updateMetadataResponseDataSerializers: Dict[int, ClassSerializer[UpdateMetadataResponseData]] = {
    version: ClassSerializer(UpdateMetadataResponseData, schema)
    for version, schema in updateMetadataResponseDataSchemas.items()
}

updateMetadataResponseDataSerializers[-1] = updateMetadataResponseDataSerializers[5]
