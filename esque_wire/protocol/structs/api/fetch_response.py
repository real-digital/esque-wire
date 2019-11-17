
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class AbortedTransaction:
    """
    :param producer_id: The producer id associated with the aborted transactions
    :type producer_id: int
    :param first_offset: The first offset in the aborted transaction
    :type first_offset: int
    """
    
    producer_id: int
    first_offset: int


@dataclass
class PartitionHeader:
    """
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: int
    :param high_watermark: Last committed offset.
    :type high_watermark: int
    :param last_stable_offset: The last stable offset (or LSO) of the partition. This is the last offset such that the
                               state of all transactional records prior to this offset have been decided (ABORTED or
                               COMMITTED)
    :type last_stable_offset: int
    :param log_start_offset: Earliest available offset.
    :type log_start_offset: int
    :param aborted_transactions: None
    :type aborted_transactions: List[AbortedTransaction]
    :param preferred_read_replica: The ID of the replica that the consumer should prefer.
    :type preferred_read_replica: int
    """
    
    partition: int
    error_code: int
    high_watermark: int
    last_stable_offset: int
    log_start_offset: int
    aborted_transactions: List[AbortedTransaction]
    preferred_read_replica: int


@dataclass
class PartitionResponse:
    """
    :param partition_header: None
    :type partition_header: PartitionHeader
    :param record_set: None
    :type record_set: Optional[bytes]
    """
    
    partition_header: PartitionHeader
    record_set: Optional[bytes]


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
class FetchResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param error_code: Response error code
    :type error_code: int
    :param session_id: The fetch session ID
    :type session_id: int
    :param responses: None
    :type responses: List[Response]
    """
    
    throttle_time_ms: int
    error_code: int
    session_id: int
    responses: List[Response]

    @staticmethod
    def api_key() -> int:
        """
        :return: `1`, the api key for this API.
        """
        return ApiKey.FETCH

