from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class Topic:
    """
    :param name: The topic name.
    :type name: str
    """

    name: str


@dataclass
class MetadataRequestData(RequestData):
    """
    :param topics: The topics to fetch metadata for.
    :type topics: List[Topic]
    :param allow_auto_topic_creation: If this is true, the broker may auto-create topics that we requested which do not
                                      already exist, if it is configured to do so.
    :type allow_auto_topic_creation: bool
    :param include_cluster_authorized_operations: Whether to include cluster authorized operations.
    :type include_cluster_authorized_operations: bool
    :param include_topic_authorized_operations: Whether to include topic authorized operations.
    :type include_topic_authorized_operations: bool
    """

    topics: List[Topic]
    allow_auto_topic_creation: bool
    include_cluster_authorized_operations: bool
    include_topic_authorized_operations: bool

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.METADATA` (`ApiKey(3)`)
        """
        return ApiKey.METADATA
