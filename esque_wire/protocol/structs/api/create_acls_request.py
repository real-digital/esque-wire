from typing import List
from dataclasses import dataclass

from ...constants import AclOperation, AclPermissionType, ApiKey, ResourceType
from ..base import RequestData


@dataclass
class Creation:
    """
    :param resource_type: The resource type
    :type resource_type: ResourceType
    :param resource_name: The resource name
    :type resource_name: str
    :param resource_pattern_type: The resource pattern type
    :type resource_pattern_type: int
    :param principal: The ACL principal
    :type principal: str
    :param host: The ACL host
    :type host: str
    :param operation: The ACL operation
    :type operation: AclOperation
    :param permission_type: The ACL permission type
    :type permission_type: AclPermissionType
    """

    resource_type: ResourceType
    resource_name: str
    resource_pattern_type: int
    principal: str
    host: str
    operation: AclOperation
    permission_type: AclPermissionType


@dataclass
class CreateAclsRequestData(RequestData):
    """
    :param creations: None
    :type creations: List[Creation]
    """

    creations: List[Creation]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.CREATE_ACLS` (`ApiKey(30)`)
        """
        return ApiKey.CREATE_ACLS
