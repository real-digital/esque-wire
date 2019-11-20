from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Resource:
    """
    :param error_code: Response error code
    :type error_code: int
    :param error_message: Response error message
    :type error_message: Optional[str]
    :param resource_type: None
    :type resource_type: int
    :param resource_name: None
    :type resource_name: str
    """

    error_code: int
    error_message: Optional[str]
    resource_type: int
    resource_name: str


@dataclass
class AlterConfigsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param resources: None
    :type resources: List[Resource]
    """

    throttle_time_ms: int
    resources: List[Resource]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `33`, the api key for this API.
        """
        return ApiKey.ALTER_CONFIGS
