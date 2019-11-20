from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class ExpireDelegationTokenResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param expiry_timestamp: timestamp (in msec) at which this token expires..
    :type expiry_timestamp: int
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    """

    error_code: ErrorCode
    expiry_timestamp: int
    throttle_time_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.EXPIRE_DELEGATION_TOKEN` (`ApiKey(40)`)
        """
        return ApiKey.EXPIRE_DELEGATION_TOKEN
