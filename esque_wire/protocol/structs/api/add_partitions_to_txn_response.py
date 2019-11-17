
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class PartitionError:
    """
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: int
    """
    
    partition: int
    error_code: int


@dataclass
class Error:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition_errors: None
    :type partition_errors: List[PartitionError]
    """
    
    topic: str
    partition_errors: List[PartitionError]


@dataclass
class AddPartitionsToTxnResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param errors: None
    :type errors: List[Error]
    """
    
    throttle_time_ms: int
    errors: List[Error]

    @staticmethod
    def api_key() -> int:
        """
        :return: `24`, the api key for this API.
        """
        return ApiKey.ADD_PARTITIONS_TO_TXN

