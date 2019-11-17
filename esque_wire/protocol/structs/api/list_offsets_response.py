
from typing import Dict, List, Optional

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
    :param timestamp: The timestamp associated with the returned offset
    :type timestamp: int
    :param offset: The offset found
    :type offset: int
    :param leader_epoch: The leader epoch
    :type leader_epoch: int
    """
    
    partition: int
    error_code: int
    timestamp: int
    offset: int
    leader_epoch: int


@dataclass
class Response:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition_responses: The listed offsets by partition
    :type partition_responses: List[PartitionResponse]
    """
    
    topic: str
    partition_responses: List[PartitionResponse]


@dataclass
class ListOffsetsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param responses: The listed offsets by topic
    :type responses: List[Response]
    """
    
    throttle_time_ms: int
    responses: List[Response]

    @staticmethod
    def api_key() -> int:
        """
        :return: `2`, the api key for this API.
        """
        return ApiKey.LIST_OFFSETS

