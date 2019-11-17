
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class TopicPartition:
    """
    :param topic: The name of a topic.
    :type topic: str
    :param partition_id: The partitions of this topic whose preferred leader should be elected
    :type partition_id: List[int]
    """
    
    topic: str
    partition_id: List[int]


@dataclass
class ElectPreferredLeadersRequestData(RequestData):
    """
    :param topic_partitions: The topic partitions to elect the preferred leader of.
    :type topic_partitions: List[TopicPartition]
    :param timeout_ms: The time in ms to wait for the election to complete.
    :type timeout_ms: int
    """
    
    topic_partitions: List[TopicPartition]
    timeout_ms: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `43`, the api key for this API.
        """
        return ApiKey.ELECT_PREFERRED_LEADERS

