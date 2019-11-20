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
        :return: `16`, the api key for this API.
        """
        return ApiKey.LIST_GROUPS