from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class LeaveGroupRequestData(RequestData):
    """
    :param group_id: The ID of the group to leave.
    :type group_id: str
    :param member_id: The member ID to remove from the group.
    :type member_id: str
    """

    group_id: str
    member_id: str

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.LEAVE_GROUP` (`ApiKey(13)`)
        """
        return ApiKey.LEAVE_GROUP
