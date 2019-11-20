from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Member:
    """
    :param member_id: The group member ID.
    :type member_id: str
    :param group_instance_id: The unique identifier of the consumer instance provided by end user.
    :type group_instance_id: Optional[str]
    :param metadata: The group member metadata.
    :type metadata: bytes
    """

    member_id: str
    group_instance_id: Optional[str]
    metadata: bytes


@dataclass
class JoinGroupResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    :param generation_id: The generation ID of the group.
    :type generation_id: int
    :param protocol_name: The group protocol selected by the coordinator.
    :type protocol_name: str
    :param leader: The leader of the group.
    :type leader: str
    :param member_id: The member ID assigned by the group coordinator.
    :type member_id: str
    :param members: 
    :type members: List[Member]
    """

    throttle_time_ms: int
    error_code: int
    generation_id: int
    protocol_name: str
    leader: str
    member_id: str
    members: List[Member]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `11`, the api key for this API.
        """
        return ApiKey.JOIN_GROUP
