
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class HeartbeatRequestData(RequestData):
    """
    :param group_id: The group id.
    :type group_id: str
    :param generation_id: The generation of the group.
    :type generation_id: int
    :param member_id: The member ID.
    :type member_id: str
    :param group_instance_id: The unique identifier of the consumer instance provided by end user.
    :type group_instance_id: Optional[str]
    """
    
    group_id: str
    generation_id: int
    member_id: str
    group_instance_id: Optional[str]

    @staticmethod
    def api_key() -> int:
        """
        :return: `12`, the api key for this API.
        """
        return ApiKey.HEARTBEAT

