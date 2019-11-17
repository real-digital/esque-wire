
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class Response:
    """
    :param name: The topic name
    :type name: str
    :param error_code: The deletion error, or 0 if the deletion succeeded.
    :type error_code: int
    """
    
    name: str
    error_code: int


@dataclass
class DeleteTopicsResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param responses: The results for each topic we tried to delete.
    :type responses: List[Response]
    """
    
    throttle_time_ms: int
    responses: List[Response]

    @staticmethod
    def api_key() -> int:
        """
        :return: `20`, the api key for this API.
        """
        return ApiKey.DELETE_TOPICS

