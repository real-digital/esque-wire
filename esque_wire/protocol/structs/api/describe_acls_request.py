from typing import Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class DescribeAclsRequestData(RequestData):
    """
    :param resource_type: The resource type
    :type resource_type: int
    :param resource_name: The resource name filter
    :type resource_name: Optional[str]
    :param resource_pattern_type_filter: The resource pattern type filter
    :type resource_pattern_type_filter: int
    :param principal: The ACL principal filter
    :type principal: Optional[str]
    :param host: The ACL host filter
    :type host: Optional[str]
    :param operation: The ACL operation
    :type operation: int
    :param permission_type: The ACL permission type
    :type permission_type: int
    """

    resource_type: int
    resource_name: Optional[str]
    resource_pattern_type_filter: int
    principal: Optional[str]
    host: Optional[str]
    operation: int
    permission_type: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `29`, the api key for this API.
        """
        return ApiKey.DESCRIBE_ACLS
