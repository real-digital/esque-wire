from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Config:
    """
    :param name: The configuration name.
    :type name: str
    :param value: The configuration value.
    :type value: Optional[str]
    """

    name: str
    value: Optional[str]


@dataclass
class Assignment:
    """
    :param partition_index: The partition index.
    :type partition_index: int
    :param broker_ids: The brokers to place the partition on.
    :type broker_ids: List[int]
    """

    partition_index: int
    broker_ids: List[int]


@dataclass
class Topic:
    """
    :param name: The topic name.
    :type name: str
    :param num_partitions: The number of partitions to create in the topic, or -1 if we are specifying a manual
                           partition assignment.
    :type num_partitions: int
    :param replication_factor: The number of replicas to create for each partition in the topic, or -1 if we are
                               specifying a manual partition assignment.
    :type replication_factor: int
    :param assignments: The manual partition assignment, or the empty array if we are using automatic assignment.
    :type assignments: List[Assignment]
    :param configs: The custom topic configurations to set.
    :type configs: List[Config]
    """

    name: str
    num_partitions: int
    replication_factor: int
    assignments: List[Assignment]
    configs: List[Config]


@dataclass
class CreateTopicsRequestData(RequestData):
    """
    :param topics: The topics to create.
    :type topics: List[Topic]
    :param timeout_ms: How long to wait in milliseconds before timing out the request.
    :type timeout_ms: int
    :param validate_only: If true, check that the topics can be created as specified, but don't create anything.
    :type validate_only: bool
    """

    topics: List[Topic]
    timeout_ms: int
    validate_only: bool

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `19`, the api key for this API.
        """
        return ApiKey.CREATE_TOPICS
