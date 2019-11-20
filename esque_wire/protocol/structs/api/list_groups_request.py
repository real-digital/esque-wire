from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class ListGroupsRequestData(RequestData):
    """
    """

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.LIST_GROUPS` (`ApiKey(16)`)
        """
        return ApiKey.LIST_GROUPS
