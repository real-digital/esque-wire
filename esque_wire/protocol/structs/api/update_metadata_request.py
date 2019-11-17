
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class EndPoint:
    """
    :param port: The port on which the broker accepts requests.
    :type port: int
    :param host: The hostname of the broker.
    :type host: str
    :param listener_name: The listener name.
    :type listener_name: str
    :param security_protocol_type: The security protocol type.
    :type security_protocol_type: int
    """
    
    port: int
    host: str
    listener_name: str
    security_protocol_type: int


@dataclass
class LiveBroker:
    """
    :param id: The broker id
    :type id: int
    :param end_points: The endpoints
    :type end_points: List[EndPoint]
    :param rack: The rack
    :type rack: Optional[str]
    """
    
    id: int
    end_points: List[EndPoint]
    rack: Optional[str]


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
    :param offline_replicas: The offline replica ids
    :type offline_replicas: List[int]
    """
    
    partition: int
    controller_epoch: int
    leader: int
    leader_epoch: int
    isr: List[int]
    zk_version: int
    replicas: List[int]
    offline_replicas: List[int]


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
class UpdateMetadataRequestData(RequestData):
    """
    :param controller_id: The controller id
    :type controller_id: int
    :param controller_epoch: The controller epoch
    :type controller_epoch: int
    :param broker_epoch: The broker epoch
    :type broker_epoch: int
    :param topic_states: Topic states
    :type topic_states: List[TopicState]
    :param live_brokers: Live broekrs
    :type live_brokers: List[LiveBroker]
    """
    
    controller_id: int
    controller_epoch: int
    broker_epoch: int
    topic_states: List[TopicState]
    live_brokers: List[LiveBroker]

    @staticmethod
    def api_key() -> int:
        """
        :return: `6`, the api key for this API.
        """
        return ApiKey.UPDATE_METADATA

