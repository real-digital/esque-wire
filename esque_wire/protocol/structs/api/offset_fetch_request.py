from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    """

    partition: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: Partitions to fetch offsets.
    :type partitions: List[Partition]
    """

    topic: str
    partitions: List[Partition]


@dataclass
class OffsetFetchRequestData(RequestData):
    """
    :param group_id: The unique group identifier
    :type group_id: str
    :param topics: Topics to fetch offsets. If the topic array is null fetch offsets for all topics.
    :type topics: List[Topic]
    """

    group_id: str
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.OFFSET_FETCH` (`ApiKey(9)`)
        """
        return ApiKey.OFFSET_FETCH
