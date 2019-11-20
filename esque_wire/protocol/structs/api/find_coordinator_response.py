from typing import Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class FindCoordinatorResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    :param error_message: The error message, or null if there was no error.
    :type error_message: Optional[str]
    :param node_id: The node id.
    :type node_id: int
    :param host: The host name.
    :type host: str
    :param port: The port.
    :type port: int
    """

    throttle_time_ms: int
    error_code: int
    error_message: Optional[str]
    node_id: int
    host: str
    port: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `10`, the api key for this API.
        """
        return ApiKey.FIND_COORDINATOR
