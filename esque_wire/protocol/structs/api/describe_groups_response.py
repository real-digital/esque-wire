from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Member:
    """
    :param member_id: The member ID assigned by the group coordinator.
    :type member_id: str
    :param client_id: The client ID used in the member's latest join group request.
    :type client_id: str
    :param client_host: The client host.
    :type client_host: str
    :param member_metadata: The metadata corresponding to the current group protocol in use.
    :type member_metadata: bytes
    :param member_assignment: The current assignment provided by the group leader.
    :type member_assignment: bytes
    """

    member_id: str
    client_id: str
    client_host: str
    member_metadata: bytes
    member_assignment: bytes


@dataclass
class Group:
    """
    :param error_code: The describe error, or 0 if there was no error.
    :type error_code: int
    :param group_id: The group ID string.
    :type group_id: str
    :param group_state: The group state string, or the empty string.
    :type group_state: str
    :param protocol_type: The group protocol type, or the empty string.
    :type protocol_type: str
    :param protocol_data: The group protocol data, or the empty string.
    :type protocol_data: str
    :param members: The group members.
    :type members: List[Member]
    :param authorized_operations: 32-bit bitfield to represent authorized operations for this group.
    :type authorized_operations: int
    """

    error_code: int
    group_id: str
    group_state: str
    protocol_type: str
    protocol_data: str
    members: List[Member]
    authorized_operations: int


@dataclass
class DescribeGroupsResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param groups: Each described group.
    :type groups: List[Group]
    """

    throttle_time_ms: int
    groups: List[Group]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `15`, the api key for this API.
        """
        return ApiKey.DESCRIBE_GROUPS
