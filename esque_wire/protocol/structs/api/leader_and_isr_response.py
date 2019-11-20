from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Partition:
    """
    :param topic: Name of topic
    :type topic: str
    :param partition: Topic partition id
    :type partition: int
    :param error_code: Response error code
    :type error_code: int
    """

    topic: str
    partition: int
    error_code: int


@dataclass
class LeaderAndIsrResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: int
    :param partitions: Response for the requests partitions
    :type partitions: List[Partition]
    """

    error_code: int
    partitions: List[Partition]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `4`, the api key for this API.
        """
        return ApiKey.LEADER_AND_ISR
