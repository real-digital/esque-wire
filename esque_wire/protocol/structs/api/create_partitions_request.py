
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class NewPartitions:
    """
    :param count: The new partition count.
    :type count: int
    :param assignment: The assigned brokers.
    :type assignment: List[List[int]]
    """
    
    count: int
    assignment: List[List[int]]


@dataclass
class TopicPartition:
    """
    :param topic: Name of topic
    :type topic: str
    :param new_partitions: None
    :type new_partitions: NewPartitions
    """
    
    topic: str
    new_partitions: NewPartitions


@dataclass
class CreatePartitionsRequestData(RequestData):
    """
    :param topic_partitions: List of topic and the corresponding new partitions.
    :type topic_partitions: List[TopicPartition]
    :param timeout: The time in ms to wait for the partitions to be created.
    :type timeout: int
    :param validate_only: If true then validate the request, but don't actually increase the number of partitions.
    :type validate_only: bool
    """
    
    topic_partitions: List[TopicPartition]
    timeout: int
    validate_only: bool

    @staticmethod
    def api_key() -> int:
        """
        :return: `37`, the api key for this API.
        """
        return ApiKey.CREATE_PARTITIONS

