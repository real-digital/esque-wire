from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Assignment:
    """
    :param member_id: The ID of the member to assign.
    :type member_id: str
    :param assignment: The member assignment.
    :type assignment: bytes
    """

    member_id: str
    assignment: bytes


@dataclass
class SyncGroupRequestData(RequestData):
    """
    :param group_id: The unique group identifier.
    :type group_id: str
    :param generation_id: The generation of the group.
    :type generation_id: int
    :param member_id: The member ID assigned by the group.
    :type member_id: str
    :param group_instance_id: The unique identifier of the consumer instance provided by end user.
    :type group_instance_id: Optional[str]
    :param assignments: Each assignment.
    :type assignments: List[Assignment]
    """

    group_id: str
    generation_id: int
    member_id: str
    group_instance_id: Optional[str]
    assignments: List[Assignment]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.SYNC_GROUP` (`ApiKey(14)`)
        """
        return ApiKey.SYNC_GROUP
