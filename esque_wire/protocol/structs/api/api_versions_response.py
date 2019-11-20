from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class ApiVersion:
    """
    :param api_key: API key.
    :type api_key: ApiKey
    :param min_version: Minimum supported version.
    :type min_version: int
    :param max_version: Maximum supported version.
    :type max_version: int
    """

    api_key: ApiKey
    min_version: int
    max_version: int


@dataclass
class ApiVersionsResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param api_versions: API versions supported by the broker.
    :type api_versions: List[ApiVersion]
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    """

    error_code: ErrorCode
    api_versions: List[ApiVersion]
    throttle_time_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.API_VERSIONS` (`ApiKey(18)`)
        """
        return ApiKey.API_VERSIONS
