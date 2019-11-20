from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: ErrorCode
    """

    topic: str
    partition: int
    error_code: ErrorCode


@dataclass
class StopReplicaResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param partitions: Response for the requests partitions
    :type partitions: List[Partition]
    """

    error_code: ErrorCode
    partitions: List[Partition]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.STOP_REPLICA` (`ApiKey(5)`)
        """
        return ApiKey.STOP_REPLICA
