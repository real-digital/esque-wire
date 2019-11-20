from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class RemainingPartition:
    """
    :param topic_name: The name of the topic.
    :type topic_name: str
    :param partition_index: The index of the partition.
    :type partition_index: int
    """

    topic_name: str
    partition_index: int


@dataclass
class ControlledShutdownResponseData(ResponseData):
    """
    :param error_code: The top-level error code.
    :type error_code: int
    :param remaining_partitions: The partitions that the broker still leads.
    :type remaining_partitions: List[RemainingPartition]
    """

    error_code: int
    remaining_partitions: List[RemainingPartition]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `7`, the api key for this API.
        """
        return ApiKey.CONTROLLED_SHUTDOWN
