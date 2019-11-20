from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param size: The size of the log segments of the partition in bytes.
    :type size: int
    :param offset_lag: The lag of the log's LEO w.r.t. partition's HW (if it is the current log for the partition) or
                       current replica's LEO (if it is the future log for the partition)
    :type offset_lag: int
    :param is_future: True if this log is created by AlterReplicaLogDirsRequest and will replace the current log of the
                      replica in the future.
    :type is_future: bool
    """

    partition: int
    size: int
    offset_lag: int
    is_future: bool


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: None
    :type partitions: List[Partition]
    """

    topic: str
    partitions: List[Partition]


@dataclass
class LogDir:
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param log_dir: The absolute log directory path.
    :type log_dir: str
    :param topics: None
    :type topics: List[Topic]
    """

    error_code: ErrorCode
    log_dir: str
    topics: List[Topic]


@dataclass
class DescribeLogDirsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param log_dirs: None
    :type log_dirs: List[LogDir]
    """

    throttle_time_ms: int
    log_dirs: List[LogDir]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DESCRIBE_LOG_DIRS` (`ApiKey(35)`)
        """
        return ApiKey.DESCRIBE_LOG_DIRS
