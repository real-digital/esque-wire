
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class MatchingAcl:
    """
    :param error_code: Response error code
    :type error_code: int
    :param error_message: Response error message
    :type error_message: Optional[str]
    :param resource_type: The resource type
    :type resource_type: int
    :param resource_name: The resource name
    :type resource_name: str
    :param resource_pattern_type: The resource pattern type
    :type resource_pattern_type: int
    :param principal: The ACL principal
    :type principal: str
    :param host: The ACL host
    :type host: str
    :param operation: The ACL operation
    :type operation: int
    :param permission_type: The ACL permission type
    :type permission_type: int
    """
    
    error_code: int
    error_message: Optional[str]
    resource_type: int
    resource_name: str
    resource_pattern_type: int
    principal: str
    host: str
    operation: int
    permission_type: int


@dataclass
class FilterResponse:
    """
    :param error_code: Response error code
    :type error_code: int
    :param error_message: Response error message
    :type error_message: Optional[str]
    :param matching_acls: The matching ACLs
    :type matching_acls: List[MatchingAcl]
    """
    
    error_code: int
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
    def api_key() -> int:
        """
        :return: `31`, the api key for this API.
        """
        return ApiKey.DELETE_ACLS

