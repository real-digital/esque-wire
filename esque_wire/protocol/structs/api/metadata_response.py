from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param error_code: The partition error, or 0 if there was no error.
    :type error_code: ErrorCode
    :param partition_index: The partition index.
    :type partition_index: int
    :param leader_id: The ID of the leader broker.
    :type leader_id: int
    :param leader_epoch: The leader epoch of this partition.
    :type leader_epoch: int
    :param replica_nodes: The set of all nodes that host this partition.
    :type replica_nodes: List[int]
    :param isr_nodes: The set of nodes that are in sync with the leader for this partition.
    :type isr_nodes: List[int]
    :param offline_replicas: The set of offline replicas of this partition.
    :type offline_replicas: List[int]
    """

    error_code: ErrorCode
    partition_index: int
    leader_id: int
    leader_epoch: int
    replica_nodes: List[int]
    isr_nodes: List[int]
    offline_replicas: List[int]


@dataclass
class Topic:
    """
    :param error_code: The topic error, or 0 if there was no error.
    :type error_code: ErrorCode
    :param name: The topic name.
    :type name: str
    :param is_internal: True if the topic is internal.
    :type is_internal: bool
    :param partitions: Each partition in the topic.
    :type partitions: List[Partition]
    :param topic_authorized_operations: 32-bit bitfield to represent authorized operations for this topic.
    :type topic_authorized_operations: int
    """

    error_code: ErrorCode
    name: str
    is_internal: bool
    partitions: List[Partition]
    topic_authorized_operations: int


@dataclass
class Broker:
    """
    :param node_id: The broker ID.
    :type node_id: int
    :param host: The broker hostname.
    :type host: str
    :param port: The broker port.
    :type port: int
    :param rack: The rack of the broker, or null if it has not been assigned to a rack.
    :type rack: Optional[str]
    """

    node_id: int
    host: str
    port: int
    rack: Optional[str]


@dataclass
class MetadataResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param brokers: Each broker in the response.
    :type brokers: List[Broker]
    :param cluster_id: The cluster ID that responding broker belongs to.
    :type cluster_id: Optional[str]
    :param controller_id: The ID of the controller broker.
    :type controller_id: int
    :param topics: Each topic in the response.
    :type topics: List[Topic]
    :param cluster_authorized_operations: 32-bit bitfield to represent authorized operations for this cluster.
    :type cluster_authorized_operations: int
    """

    throttle_time_ms: int
    brokers: List[Broker]
    cluster_id: Optional[str]
    controller_id: int
    topics: List[Topic]
    cluster_authorized_operations: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.METADATA` (`ApiKey(3)`)
        """
        return ApiKey.METADATA
