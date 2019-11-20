from typing import Optional
from dataclasses import dataclass

from ...constants import AclOperation, AclPermissionType, ApiKey, ResourceType
from ..base import RequestData


@dataclass
class DescribeAclsRequestData(RequestData):
    """
    :param resource_type: The resource type
    :type resource_type: ResourceType
    :param resource_name: The resource name filter
    :type resource_name: Optional[str]
    :param resource_pattern_type_filter: The resource pattern type filter
    :type resource_pattern_type_filter: int
    :param principal: The ACL principal filter
    :type principal: Optional[str]
    :param host: The ACL host filter
    :type host: Optional[str]
    :param operation: The ACL operation
    :type operation: AclOperation
    :param permission_type: The ACL permission type
    :type permission_type: AclPermissionType
    """

    resource_type: ResourceType
    resource_name: Optional[str]
    resource_pattern_type_filter: int
    principal: Optional[str]
    host: Optional[str]
    operation: AclOperation
    permission_type: AclPermissionType

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DESCRIBE_ACLS` (`ApiKey(29)`)
        """
        return ApiKey.DESCRIBE_ACLS
