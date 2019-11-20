from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Data:
    """
    :param partition: Topic partition id
    :type partition: int
    :param record_set: None
    :type record_set: Optional[bytes]
    """

    partition: int
    record_set: Optional[bytes]


@dataclass
class TopicData:
    """
    :param topic: Name of topic
    :type topic: str
    :param data: None
    :type data: List[Data]
    """

    topic: str
    data: List[Data]


@dataclass
class ProduceRequestData(RequestData):
    """
    :param transactional_id: The transactional id or null if the producer is not transactional
    :type transactional_id: Optional[str]
    :param acks: The number of acknowledgments the producer requires the leader to have received before considering a
                 request complete. Allowed values: 0 for no acknowledgments, 1 for only the leader and -1 for the full
                 ISR.
    :type acks: int
    :param timeout: The time to await a response in ms.
    :type timeout: int
    :param topic_data: None
    :type topic_data: List[TopicData]
    """

    transactional_id: Optional[str]
    acks: int
    timeout: int
    topic_data: List[TopicData]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.PRODUCE` (`ApiKey(0)`)
        """
        return ApiKey.PRODUCE
