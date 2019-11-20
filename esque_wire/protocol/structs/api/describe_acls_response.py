from typing import List, Optional
from dataclasses import dataclass

from ...constants import (
    AclOperation,
    AclPermissionType,
    ApiKey,
    ErrorCode,
    ResourceType,
)
from ..base import ResponseData


@dataclass
class Acl:
    """
    :param principal: The ACL principal
    :type principal: str
    :param host: The ACL host
    :type host: str
    :param operation: The ACL operation
    :type operation: AclOperation
    :param permission_type: The ACL permission type
    :type permission_type: AclPermissionType
    """

    principal: str
    host: str
    operation: AclOperation
    permission_type: AclPermissionType


@dataclass
class Resource:
    """
    :param resource_type: The resource type
    :type resource_type: ResourceType
    :param resource_name: The resource name
    :type resource_name: str
    :param resource_pattern_type: The resource pattern type
    :type resource_pattern_type: int
    :param acls: None
    :type acls: List[Acl]
    """

    resource_type: ResourceType
    resource_name: str
    resource_pattern_type: int
    acls: List[Acl]


@dataclass
class DescribeAclsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param error_message: Response error message
    :type error_message: Optional[str]
    :param resources: The resources and their associated ACLs.
    :type resources: List[Resource]
    """

    throttle_time_ms: int
    error_code: ErrorCode
    error_message: Optional[str]
    resources: List[Resource]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DESCRIBE_ACLS` (`ApiKey(29)`)
        """
        return ApiKey.DESCRIBE_ACLS
