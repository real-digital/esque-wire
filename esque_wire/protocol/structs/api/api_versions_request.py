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
        :return: `18`, the api key for this API.
        """
        return ApiKey.API_VERSIONS
