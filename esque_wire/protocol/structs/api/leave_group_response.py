from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class LeaveGroupResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: ErrorCode
    """

    throttle_time_ms: int
    error_code: ErrorCode

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.LEAVE_GROUP` (`ApiKey(13)`)
        """
        return ApiKey.LEAVE_GROUP
