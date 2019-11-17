
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class Protocol:
    """
    :param name: The protocol name.
    :type name: str
    :param metadata: The protocol metadata.
    :type metadata: bytes
    """
    
    name: str
    metadata: bytes


@dataclass
class JoinGroupRequestData(RequestData):
    """
    :param group_id: The group identifier.
    :type group_id: str
    :param session_timeout_ms: The coordinator considers the consumer dead if it receives no heartbeat after this
                               timeout in milliseconds.
    :type session_timeout_ms: int
    :param rebalance_timeout_ms: The maximum time in milliseconds that the coordinator will wait for each member to
                                 rejoin when rebalancing the group.
    :type rebalance_timeout_ms: int
    :param member_id: The member id assigned by the group coordinator.
    :type member_id: str
    :param group_instance_id: The unique identifier of the consumer instance provided by end user.
    :type group_instance_id: Optional[str]
    :param protocol_type: The unique name the for class of protocols implemented by the group we want to join.
    :type protocol_type: str
    :param protocols: The list of protocols that the member supports.
    :type protocols: List[Protocol]
    """
    
    group_id: str
    session_timeout_ms: int
    rebalance_timeout_ms: int
    member_id: str
    group_instance_id: Optional[str]
    protocol_type: str
    protocols: List[Protocol]

    @staticmethod
    def api_key() -> int:
        """
        :return: `11`, the api key for this API.
        """
        return ApiKey.JOIN_GROUP

