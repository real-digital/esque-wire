from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Partition:
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
    """

    partition: int
    offset: int
    leader_epoch: int
    metadata: Optional[str]


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: Partitions to commit offsets
    :type partitions: List[Partition]
    """

    topic: str
    partitions: List[Partition]


@dataclass
class TxnOffsetCommitRequestData(RequestData):
    """
    :param transactional_id: The transactional id corresponding to the transaction.
    :type transactional_id: str
    :param group_id: The unique group identifier
    :type group_id: str
    :param producer_id: Current producer id in use by the transactional id.
    :type producer_id: int
    :param producer_epoch: Current epoch associated with the producer id.
    :type producer_epoch: int
    :param topics: Topics to commit offsets
    :type topics: List[Topic]
    """

    transactional_id: str
    group_id: str
    producer_id: int
    producer_epoch: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `28`, the api key for this API.
        """
        return ApiKey.TXN_OFFSET_COMMIT
