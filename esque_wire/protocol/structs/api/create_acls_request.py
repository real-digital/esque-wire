
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class Creation:
    """
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
    
    resource_type: int
    resource_name: str
    resource_pattern_type: int
    principal: str
    host: str
    operation: int
    permission_type: int


@dataclass
class CreateAclsRequestData(RequestData):
    """
    :param creations: None
    :type creations: List[Creation]
    """
    
    creations: List[Creation]

    @staticmethod
    def api_key() -> int:
        """
        :return: `30`, the api key for this API.
        """
        return ApiKey.CREATE_ACLS

