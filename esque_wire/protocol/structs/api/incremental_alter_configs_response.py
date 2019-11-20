from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Response:
    """
    :param error_code: The resource error code.
    :type error_code: int
    :param error_message: The resource error message, or null if there was no error.
    :type error_message: Optional[str]
    :param resource_type: The resource type.
    :type resource_type: int
    :param resource_name: The resource name.
    :type resource_name: str
    """

    error_code: int
    error_message: Optional[str]
    resource_type: int
    resource_name: str


@dataclass
class IncrementalAlterConfigsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to a quota violation, or
                             zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param responses: The responses for each resource.
    :type responses: List[Response]
    """

    throttle_time_ms: int
    responses: List[Response]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `44`, the api key for this API.
        """
        return ApiKey.INCREMENTAL_ALTER_CONFIGS
