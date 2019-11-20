from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class PartitionResult:
    """
    :param partition_id: The partition id
    :type partition_id: int
    :param error_code: The result error, or zero if there was no error.
    :type error_code: ErrorCode
    :param error_message: The result message, or null if there was no error.
    :type error_message: Optional[str]
    """

    partition_id: int
    error_code: ErrorCode
    error_message: Optional[str]


@dataclass
class ReplicaElectionResult:
    """
    :param topic: The topic name
    :type topic: str
    :param partition_result: The results for each partition
    :type partition_result: List[PartitionResult]
    """

    topic: str
    partition_result: List[PartitionResult]


@dataclass
class ElectPreferredLeadersResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param replica_election_results: The election results, or an empty array if the requester did not have permission
                                     and the request asks for all partitions.
    :type replica_election_results: List[ReplicaElectionResult]
    """

    throttle_time_ms: int
    replica_election_results: List[ReplicaElectionResult]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.ELECT_PREFERRED_LEADERS` (`ApiKey(43)`)
        """
        return ApiKey.ELECT_PREFERRED_LEADERS
