from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class EndTxnResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param error_code: Response error code
    :type error_code: int
    """

    throttle_time_ms: int
    error_code: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `26`, the api key for this API.
        """
        return ApiKey.END_TXN
