
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class Partition:
    """
    :param partition_index: The partition index.
    :type partition_index: int
    :param committed_offset: The message offset to be committed.
    :type committed_offset: int
    :param committed_leader_epoch: The leader epoch of this partition.
    :type committed_leader_epoch: int
    :param committed_metadata: Any associated metadata the client wants to keep.
    :type committed_metadata: Optional[str]
    """
    
    partition_index: int
    committed_offset: int
    committed_leader_epoch: int
    committed_metadata: Optional[str]


@dataclass
class Topic:
    """
    :param name: The topic name.
    :type name: str
    :param partitions: Each partition to commit offsets for.
    :type partitions: List[Partition]
    """
    
    name: str
    partitions: List[Partition]


@dataclass
class OffsetCommitRequestData(RequestData):
    """
    :param group_id: The unique group identifier.
    :type group_id: str
    :param generation_id: The generation of the group.
    :type generation_id: int
    :param member_id: The member ID assigned by the group coordinator.
    :type member_id: str
    :param group_instance_id: The unique identifier of the consumer instance provided by end user.
    :type group_instance_id: Optional[str]
    :param topics: The topics to commit offsets for.
    :type topics: List[Topic]
    """
    
    group_id: str
    generation_id: int
    member_id: str
    group_instance_id: Optional[str]
    topics: List[Topic]

    @staticmethod
    def api_key() -> int:
        """
        :return: `8`, the api key for this API.
        """
        return ApiKey.OFFSET_COMMIT

