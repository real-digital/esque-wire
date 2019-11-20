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
class MatchingAcl:
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param error_message: Response error message
    :type error_message: Optional[str]
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

    error_code: ErrorCode
    error_message: Optional[str]
    resource_type: ResourceType
    resource_name: str
    resource_pattern_type: int
    principal: str
    host: str
    operation: AclOperation
    permission_type: AclPermissionType


@dataclass
class FilterResponse:
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param error_message: Response error message
    :type error_message: Optional[str]
    :param matching_acls: The matching ACLs
    :type matching_acls: List[MatchingAcl]
    """

    error_code: ErrorCode
    error_message: Optional[str]
    matching_acls: List[MatchingAcl]


@dataclass
class DeleteAclsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param filter_responses: None
    :type filter_responses: List[FilterResponse]
    """

    throttle_time_ms: int
    filter_responses: List[FilterResponse]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DELETE_ACLS` (`ApiKey(31)`)
        """
        return ApiKey.DELETE_ACLS
