##############################################
# Autogenerated module. Please don't modify. #
##############################################

from esque_wire.protocol.serializers.generic import EnumSerializer
from esque_wire.protocol.serializers.primitive import int8Serializer, int16Serializer
from esque_wire.protocol.constants import (
    ApiKey,
    AclOperation,
    ResourceType,
    AclPermissionType,
    ResourcePatternType,
    ErrorCode,
)

apiKeySerializer = EnumSerializer(ApiKey, int16Serializer)
aclOperationSerializer = EnumSerializer(AclOperation, int8Serializer)
resourceTypeSerializer = EnumSerializer(ResourceType, int8Serializer)
aclPermissionTypeSerializer = EnumSerializer(AclPermissionType, int8Serializer)
resourcePatternTypeSerializer = EnumSerializer(ResourcePatternType, int8Serializer)
errorCodeSerializer = EnumSerializer(ErrorCode, int16Serializer)
