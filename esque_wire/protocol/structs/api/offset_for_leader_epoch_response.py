
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class Partition:
    """
    :param error_code: Response error code
    :type error_code: int
    :param partition: Topic partition id
    :type partition: int
    :param leader_epoch: The leader epoch
    :type leader_epoch: int
    :param end_offset: The end offset
    :type end_offset: int
    """
    
    error_code: int
    partition: int
    leader_epoch: int
    end_offset: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: An array of offsets by partition
    :type partitions: List[Partition]
    """
    
    topic: str
    partitions: List[Partition]


@dataclass
class OffsetForLeaderEpochResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param topics: An array of topics for which we have leader offsets for some requested partition leader epoch
    :type topics: List[Topic]
    """
    
    throttle_time_ms: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> int:
        """
        :return: `23`, the api key for this API.
        """
        return ApiKey.OFFSET_FOR_LEADER_EPOCH

