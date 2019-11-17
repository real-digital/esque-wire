
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param low_watermark: Smallest available offset of all live replicas
    :type low_watermark: int
    :param error_code: Response error code
    :type error_code: int
    """
    
    partition: int
    low_watermark: int
    error_code: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: None
    :type partitions: List[Partition]
    """
    
    topic: str
    partitions: List[Partition]


@dataclass
class DeleteRecordsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param topics: None
    :type topics: List[Topic]
    """
    
    throttle_time_ms: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> int:
        """
        :return: `21`, the api key for this API.
        """
        return ApiKey.DELETE_RECORDS

