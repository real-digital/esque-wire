from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param current_leader_epoch: The current leader epoch, if provided, is used to fence consumers/replicas with old
                                 metadata. If the epoch provided by the client is larger than the current epoch known
                                 to the broker, then the UNKNOWN_LEADER_EPOCH error code will be returned. If the
                                 provided epoch is smaller, then the FENCED_LEADER_EPOCH error code will be returned.
    :type current_leader_epoch: int
    :param timestamp: The target timestamp for the partition.
    :type timestamp: int
    """

    partition: int
    current_leader_epoch: int
    timestamp: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: Partitions to list offsets.
    :type partitions: List[Partition]
    """

    topic: str
    partitions: List[Partition]


@dataclass
class ListOffsetsRequestData(RequestData):
    """
    :param replica_id: Broker id of the follower. For normal consumers, use -1.
    :type replica_id: int
    :param isolation_level: This setting controls the visibility of transactional records. Using READ_UNCOMMITTED
                            (isolation_level = 0) makes all records visible. With READ_COMMITTED (isolation_level = 1),
                            non-transactional and COMMITTED transactional records are visible. To be more concrete,
                            READ_COMMITTED returns all data from offsets smaller than the current LSO (last stable
                            offset), and enables the inclusion of the list of aborted transactions in the result, which
                            allows consumers to discard ABORTED transactional records
    :type isolation_level: int
    :param topics: Topics to list offsets.
    :type topics: List[Topic]
    """

    replica_id: int
    isolation_level: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `2`, the api key for this API.
        """
        return ApiKey.LIST_OFFSETS
