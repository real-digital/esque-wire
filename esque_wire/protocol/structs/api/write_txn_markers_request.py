
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: None
    :type partitions: List[int]
    """
    
    topic: str
    partitions: List[int]


@dataclass
class TransactionMarker:
    """
    :param producer_id: Current producer id in use by the transactional id.
    :type producer_id: int
    :param producer_epoch: Current epoch associated with the producer id.
    :type producer_epoch: int
    :param transaction_result: The result of the transaction to write to the partitions (false = ABORT, true = COMMIT).
    :type transaction_result: bool
    :param topics: The partitions to write markers for.
    :type topics: List[Topic]
    :param coordinator_epoch: Epoch associated with the transaction state partition hosted by this transaction
                              coordinator
    :type coordinator_epoch: int
    """
    
    producer_id: int
    producer_epoch: int
    transaction_result: bool
    topics: List[Topic]
    coordinator_epoch: int


@dataclass
class WriteTxnMarkersRequestData(RequestData):
    """
    :param transaction_markers: The transaction markers to be written.
    :type transaction_markers: List[TransactionMarker]
    """
    
    transaction_markers: List[TransactionMarker]

    @staticmethod
    def api_key() -> int:
        """
        :return: `27`, the api key for this API.
        """
        return ApiKey.WRITE_TXN_MARKERS

