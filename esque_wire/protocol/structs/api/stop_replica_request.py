
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class Partition:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition_ids: The partition ids of a topic
    :type partition_ids: List[int]
    """
    
    topic: str
    partition_ids: List[int]


@dataclass
class StopReplicaRequestData(RequestData):
    """
    :param controller_id: The controller id
    :type controller_id: int
    :param controller_epoch: The controller epoch
    :type controller_epoch: int
    :param broker_epoch: The broker epoch
    :type broker_epoch: int
    :param delete_partitions: Boolean which indicates if replica's partitions must be deleted.
    :type delete_partitions: bool
    :param partitions: The partitions
    :type partitions: List[Partition]
    """
    
    controller_id: int
    controller_epoch: int
    broker_epoch: int
    delete_partitions: bool
    partitions: List[Partition]

    @staticmethod
    def api_key() -> int:
        """
        :return: `5`, the api key for this API.
        """
        return ApiKey.STOP_REPLICA

