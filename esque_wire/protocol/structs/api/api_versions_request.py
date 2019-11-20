from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class ApiVersionsRequestData(RequestData):
    """
    """

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.API_VERSIONS` (`ApiKey(18)`)
        """
        return ApiKey.API_VERSIONS
