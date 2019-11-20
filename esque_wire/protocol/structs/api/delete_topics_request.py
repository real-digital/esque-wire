from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class DeleteTopicsRequestData(RequestData):
    """
    :param topic_names: The names of the topics to delete
    :type topic_names: List[str]
    :param timeout_ms: The length of time in milliseconds to wait for the deletions to complete.
    :type timeout_ms: int
    """

    topic_names: List[str]
    timeout_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `20`, the api key for this API.
        """
        return ApiKey.DELETE_TOPICS
