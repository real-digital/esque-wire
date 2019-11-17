
from typing import Dict, List, Optional

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
    :param partitions: None
    :type partitions: List[Partition]
    """
    
    topic: str
    partitions: List[Partition]


@dataclass
class AlterReplicaLogDirsResponseData(ResponseData):
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
        :return: `34`, the api key for this API.
        """
        return ApiKey.ALTER_REPLICA_LOG_DIRS

