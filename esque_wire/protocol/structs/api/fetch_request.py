from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class ForgottenTopicsData:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: Partitions to remove from the fetch session.
    :type partitions: List[int]
    """

    topic: str
    partitions: List[int]


@dataclass
class Partition:
    """
    :param partition: Topic partition id
    :type partition: int
    :param current_leader_epoch: The current leader epoch, if provided, is used to fence consumers/replicas with old
                                 metadata. If the epoch provided by the client is larger than the current epoch known
                                 to the broker, then the UNKNOWN_LEADER_EPOCH error code will be returned. If the
                                 provided epoch is smaller, then the FENCED_LEADER_EPOCH error code will be returned.
    :type current_leader_epoch: int
    :param fetch_offset: Message offset.
    :type fetch_offset: int
    :param log_start_offset: Earliest available offset of the follower replica. The field is only used when request is
                             sent by follower.
    :type log_start_offset: int
    :param partition_max_bytes: Maximum bytes to fetch.
    :type partition_max_bytes: int
    """

    partition: int
    current_leader_epoch: int
    fetch_offset: int
    log_start_offset: int
    partition_max_bytes: int


@dataclass
class Topic:
    """
    :param topic: Name of topic
    :type topic: str
    :param partitions: Partitions to fetch.
    :type partitions: List[Partition]
    """

    topic: str
    partitions: List[Partition]


@dataclass
class FetchRequestData(RequestData):
    """
    :param replica_id: Broker id of the follower. For normal consumers, use -1.
    :type replica_id: int
    :param max_wait_time: Maximum time in ms to wait for the response.
    :type max_wait_time: int
    :param min_bytes: Minimum bytes to accumulate in the response.
    :type min_bytes: int
    :param max_bytes: Maximum bytes to accumulate in the response. Note that this is not an absolute maximum, if the
                      first message in the first non-empty partition of the fetch is larger than this value, the
                      message will still be returned to ensure that progress can be made.
    :type max_bytes: int
    :param isolation_level: This setting controls the visibility of transactional records. Using READ_UNCOMMITTED
                            (isolation_level = 0) makes all records visible. With READ_COMMITTED (isolation_level = 1),
                            non-transactional and COMMITTED transactional records are visible. To be more concrete,
                            READ_COMMITTED returns all data from offsets smaller than the current LSO (last stable
                            offset), and enables the inclusion of the list of aborted transactions in the result, which
                            allows consumers to discard ABORTED transactional records
    :type isolation_level: int
    :param session_id: The fetch session ID
    :type session_id: int
    :param session_epoch: The fetch session epoch
    :type session_epoch: int
    :param topics: Topics to fetch in the order provided.
    :type topics: List[Topic]
    :param forgotten_topics_data: Topics to remove from the fetch session.
    :type forgotten_topics_data: List[ForgottenTopicsData]
    :param rack_id: The consumer's rack id
    :type rack_id: str
    """

    replica_id: int
    max_wait_time: int
    min_bytes: int
    max_bytes: int
    isolation_level: int
    session_id: int
    session_epoch: int
    topics: List[Topic]
    forgotten_topics_data: List[ForgottenTopicsData]
    rack_id: str

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.FETCH` (`ApiKey(1)`)
        """
        return ApiKey.FETCH
