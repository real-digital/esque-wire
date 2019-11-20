from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class PartitionResponse:
    """
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: int
    :param base_offset: None
    :type base_offset: int
    :param log_append_time: The timestamp returned by broker after appending the messages. If CreateTime is used for
                            the topic, the timestamp will be -1. If LogAppendTime is used for the topic, the timestamp
                            will be the broker local time when the messages are appended.
    :type log_append_time: int
    :param log_start_offset: The start offset of the log at the time this produce response was created
    :type log_start_offset: int
    """

    partition: int
    error_code: int
    base_offset: int
    log_append_time: int
    log_start_offset: int


@dataclass
class Response:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition_responses: None
    :type partition_responses: List[PartitionResponse]
    """

    topic: str
    partition_responses: List[PartitionResponse]


@dataclass
class ProduceResponseData(ResponseData):
    """
    :param responses: None
    :type responses: List[Response]
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    """

    responses: List[Response]
    throttle_time_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `0`, the api key for this API.
        """
        return ApiKey.PRODUCE
