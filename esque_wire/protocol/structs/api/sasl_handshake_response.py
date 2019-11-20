from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class SaslHandshakeResponseData(ResponseData):
    """
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: ErrorCode
    :param mechanisms: The mechanisms enabled in the server.
    :type mechanisms: List[str]
    """

    error_code: ErrorCode
    mechanisms: List[str]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.SASL_HANDSHAKE` (`ApiKey(17)`)
        """
        return ApiKey.SASL_HANDSHAKE
