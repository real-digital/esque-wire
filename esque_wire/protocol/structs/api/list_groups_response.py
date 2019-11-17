
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class Group:
    """
    :param group_id: The unique group identifier
    :type group_id: str
    :param protocol_type: None
    :type protocol_type: str
    """
    
    group_id: str
    protocol_type: str


@dataclass
class ListGroupsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param error_code: Response error code
    :type error_code: int
    :param groups: None
    :type groups: List[Group]
    """
    
    throttle_time_ms: int
    error_code: int
    groups: List[Group]

    @staticmethod
    def api_key() -> int:
        """
        :return: `16`, the api key for this API.
        """
        return ApiKey.LIST_GROUPS

