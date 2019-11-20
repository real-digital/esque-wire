from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param offset: The offset before which the messages will be deleted. -1 means high-watermark for the partition.
    :type offset: int
    """

    partition: int
    offset: int


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
class DeleteRecordsRequestData(RequestData):
    """
    :param topics: None
    :type topics: List[Topic]
    :param timeout: The maximum time to await a response in ms.
    :type timeout: int
    """

    topics: List[Topic]
    timeout: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DELETE_RECORDS` (`ApiKey(21)`)
        """
        return ApiKey.DELETE_RECORDS
