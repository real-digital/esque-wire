from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: List of partition ids of the topic.
    :type partitions: List[int]
    """

    topic: str
    partitions: List[int]


@dataclass
class DescribeLogDirsRequestData(RequestData):
    """
    :param topics: None
    :type topics: List[Topic]
    """

    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `35`, the api key for this API.
        """
        return ApiKey.DESCRIBE_LOG_DIRS
