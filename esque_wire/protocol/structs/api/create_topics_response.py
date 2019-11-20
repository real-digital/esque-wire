from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Topic:
    """
    :param name: The topic name.
    :type name: str
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    :param error_message: The error message, or null if there was no error.
    :type error_message: Optional[str]
    """

    name: str
    error_code: int
    error_message: Optional[str]


@dataclass
class CreateTopicsResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param topics: Results for each topic we tried to create.
    :type topics: List[Topic]
    """

    throttle_time_ms: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `19`, the api key for this API.
        """
        return ApiKey.CREATE_TOPICS
