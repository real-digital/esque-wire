
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class ApiVersion:
    """
    :param api_key: API key.
    :type api_key: int
    :param min_version: Minimum supported version.
    :type min_version: int
    :param max_version: Maximum supported version.
    :type max_version: int
    """
    
    api_key: int
    min_version: int
    max_version: int


@dataclass
class ApiVersionsResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: int
    :param api_versions: API versions supported by the broker.
    :type api_versions: List[ApiVersion]
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    """
    
    error_code: int
    api_versions: List[ApiVersion]
    throttle_time_ms: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `18`, the api key for this API.
        """
        return ApiKey.API_VERSIONS

