from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class TopicError:
    """
    :param topic: Name of topic
    :type topic: str
    :param error_code: Response error code
    :type error_code: int
    :param error_message: Response error message
    :type error_message: Optional[str]
    """

    topic: str
    error_code: int
    error_message: Optional[str]


@dataclass
class CreatePartitionsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param topic_errors: Per topic results for the create partitions request
    :type topic_errors: List[TopicError]
    """

    throttle_time_ms: int
    topic_errors: List[TopicError]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `37`, the api key for this API.
        """
        return ApiKey.CREATE_PARTITIONS
