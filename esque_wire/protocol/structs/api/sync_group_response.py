from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class SyncGroupResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: ErrorCode
    :param assignment: The member assignment.
    :type assignment: bytes
    """

    throttle_time_ms: int
    error_code: ErrorCode
    assignment: bytes

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.SYNC_GROUP` (`ApiKey(14)`)
        """
        return ApiKey.SYNC_GROUP
