from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class DeleteGroupsRequestData(RequestData):
    """
    :param groups: An array of groups to be deleted.
    :type groups: List[str]
    """

    groups: List[str]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DELETE_GROUPS` (`ApiKey(42)`)
        """
        return ApiKey.DELETE_GROUPS
