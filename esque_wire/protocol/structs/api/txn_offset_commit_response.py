from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: int
    """

    partition: int
    error_code: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: Responses by partition for committed offsets
    :type partitions: List[Partition]
    """

    topic: str
    partitions: List[Partition]


@dataclass
class TxnOffsetCommitResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param topics: Responses by topic for committed offsets
    :type topics: List[Topic]
    """

    throttle_time_ms: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `28`, the api key for this API.
        """
        return ApiKey.TXN_OFFSET_COMMIT
