from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: ErrorCode
    """

    partition: int
    error_code: ErrorCode


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
class TransactionMarker:
    """
    :param producer_id: Current producer id in use by the transactional id.
    :type producer_id: int
    :param topics: Errors per partition from writing markers.
    :type topics: List[Topic]
    """

    producer_id: int
    topics: List[Topic]


@dataclass
class WriteTxnMarkersResponseData(ResponseData):
    """
    :param transaction_markers: Errors per partition from writing markers.
    :type transaction_markers: List[TransactionMarker]
    """

    transaction_markers: List[TransactionMarker]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.WRITE_TXN_MARKERS` (`ApiKey(27)`)
        """
        return ApiKey.WRITE_TXN_MARKERS
