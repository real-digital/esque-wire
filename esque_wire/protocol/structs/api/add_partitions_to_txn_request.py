from typing import List
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
class AddPartitionsToTxnRequestData(RequestData):
    """
    :param transactional_id: The transactional id corresponding to the transaction.
    :type transactional_id: str
    :param producer_id: Current producer id in use by the transactional id.
    :type producer_id: int
    :param producer_epoch: Current epoch associated with the producer id.
    :type producer_epoch: int
    :param topics: The partitions to add to the transaction.
    :type topics: List[Topic]
    """

    transactional_id: str
    producer_id: int
    producer_epoch: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.ADD_PARTITIONS_TO_TXN` (`ApiKey(24)`)
        """
        return ApiKey.ADD_PARTITIONS_TO_TXN
