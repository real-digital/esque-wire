from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param partition_index: The partition index.
    :type partition_index: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    """

    partition_index: int
    error_code: int


@dataclass
class Topic:
    """
    :param name: The topic name.
    :type name: str
    :param partitions: The responses for each partition in the topic.
    :type partitions: List[Partition]
    """

    name: str
    partitions: List[Partition]


@dataclass
class OffsetCommitResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param topics: The responses for each topic.
    :type topics: List[Topic]
    """

    throttle_time_ms: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `8`, the api key for this API.
        """
        return ApiKey.OFFSET_COMMIT
