from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class AddOffsetsToTxnResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param error_code: Response error code
    :type error_code: ErrorCode
    """

    throttle_time_ms: int
    error_code: ErrorCode

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.ADD_OFFSETS_TO_TXN` (`ApiKey(25)`)
        """
        return ApiKey.ADD_OFFSETS_TO_TXN
