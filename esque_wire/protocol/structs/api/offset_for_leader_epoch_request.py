
from typing import Dict, List, Optional

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
    :param leader_epoch: The epoch to lookup an offset for.
    :type leader_epoch: int
    """
    
    partition: int
    current_leader_epoch: int
    leader_epoch: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: An array of partitions to get epochs for
    :type partitions: List[Partition]
    """
    
    topic: str
    partitions: List[Partition]


@dataclass
class OffsetForLeaderEpochRequestData(RequestData):
    """
    :param replica_id: Broker id of the follower. For normal consumers, use -1.
    :type replica_id: int
    :param topics: An array of topics to get epochs for
    :type topics: List[Topic]
    """
    
    replica_id: int
    topics: List[Topic]

    @staticmethod
    def api_key() -> int:
        """
        :return: `23`, the api key for this API.
        """
        return ApiKey.OFFSET_FOR_LEADER_EPOCH

