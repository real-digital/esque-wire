from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: List of partition ids of the topic.
    :type partitions: List[int]
    """

    topic: str
    partitions: List[int]


@dataclass
class LogDir:
    """
    :param log_dir: The absolute log directory path.
    :type log_dir: str
    :param topics: None
    :type topics: List[Topic]
    """

    log_dir: str
    topics: List[Topic]


@dataclass
class AlterReplicaLogDirsRequestData(RequestData):
    """
    :param log_dirs: None
    :type log_dirs: List[LogDir]
    """

    log_dirs: List[LogDir]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.ALTER_REPLICA_LOG_DIRS` (`ApiKey(34)`)
        """
        return ApiKey.ALTER_REPLICA_LOG_DIRS
