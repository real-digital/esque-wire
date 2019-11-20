from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class HeartbeatResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    """

    throttle_time_ms: int
    error_code: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `12`, the api key for this API.
        """
        return ApiKey.HEARTBEAT
