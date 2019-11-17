
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class DescribeGroupsRequestData(RequestData):
    """
    :param groups: The names of the groups to describe
    :type groups: List[str]
    :param include_authorized_operations: Whether to include authorized operations.
    :type include_authorized_operations: bool
    """
    
    groups: List[str]
    include_authorized_operations: bool

    @staticmethod
    def api_key() -> int:
        """
        :return: `15`, the api key for this API.
        """
        return ApiKey.DESCRIBE_GROUPS

