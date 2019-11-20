from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class LiveLeader:
    """
    :param id: The broker id
    :type id: int
    :param host: The hostname of the broker.
    :type host: str
    :param port: The port on which the broker accepts requests.
    :type port: int
    """

    id: int
    host: str
    port: int


@dataclass
class PartitionState:
    """
    :param partition: Topic partition id
    :type partition: int
    :param controller_epoch: The controller epoch
    :type controller_epoch: int
    :param leader: The broker id for the leader.
    :type leader: int
    :param leader_epoch: The leader epoch.
    :type leader_epoch: int
    :param isr: The in sync replica ids.
    :type isr: List[int]
    :param zk_version: The ZK version.
    :type zk_version: int
    :param replicas: The replica ids.
    :type replicas: List[int]
    :param is_new: Whether the replica should have existed on the broker or not
    :type is_new: bool
    """

    partition: int
    controller_epoch: int
    leader: int
    leader_epoch: int
    isr: List[int]
    zk_version: int
    replicas: List[int]
    is_new: bool


@dataclass
class TopicState:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition_states: Partition states
    :type partition_states: List[PartitionState]
    """

    topic: str
    partition_states: List[PartitionState]


@dataclass
class LeaderAndIsrRequestData(RequestData):
    """
    :param controller_id: The controller id
    :type controller_id: int
    :param controller_epoch: The controller epoch
    :type controller_epoch: int
    :param broker_epoch: The broker epoch
    :type broker_epoch: int
    :param topic_states: Topic states
    :type topic_states: List[TopicState]
    :param live_leaders: Live leaders
    :type live_leaders: List[LiveLeader]
    """

    controller_id: int
    controller_epoch: int
    broker_epoch: int
    topic_states: List[TopicState]
    live_leaders: List[LiveLeader]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.LEADER_AND_ISR` (`ApiKey(4)`)
        """
        return ApiKey.LEADER_AND_ISR
