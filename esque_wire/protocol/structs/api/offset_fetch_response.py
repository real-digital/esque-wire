
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class PartitionResponse:
    """
    :param partition: Topic partition id
    :type partition: int
    :param offset: Message offset to be committed
    :type offset: int
    :param leader_epoch: The leader epoch, if provided is derived from the last consumed record. This is used by the
                         consumer to check for log truncation and to ensure partition metadata is up to date following
                         a group rebalance.
    :type leader_epoch: int
    :param metadata: Any associated metadata the client wants to keep.
    :type metadata: Optional[str]
    :param error_code: Response error code
    :type error_code: int
    """
    
    partition: int
    offset: int
    leader_epoch: int
    metadata: Optional[str]
    error_code: int


@dataclass
class Response:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition_responses: Responses by partition for fetched offsets
    :type partition_responses: List[PartitionResponse]
    """
    
    topic: str
    partition_responses: List[PartitionResponse]


@dataclass
class OffsetFetchResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param responses: Responses by topic for fetched offsets
    :type responses: List[Response]
    :param error_code: Response error code
    :type error_code: int
    """
    
    throttle_time_ms: int
    responses: List[Response]
    error_code: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `9`, the api key for this API.
        """
        return ApiKey.OFFSET_FETCH

