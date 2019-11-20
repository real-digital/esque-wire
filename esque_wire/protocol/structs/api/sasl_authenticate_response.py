from typing import Optional
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class SaslAuthenticateResponseData(ResponseData):
    """
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: ErrorCode
    :param error_message: The error message, or null if there was no error.
    :type error_message: Optional[str]
    :param auth_bytes: The SASL authentication bytes from the server, as defined by the SASL mechanism.
    :type auth_bytes: bytes
    :param session_lifetime_ms: The SASL authentication bytes from the server, as defined by the SASL mechanism.
    :type session_lifetime_ms: int
    """

    error_code: ErrorCode
    error_message: Optional[str]
    auth_bytes: bytes
    session_lifetime_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.SASL_AUTHENTICATE` (`ApiKey(36)`)
        """
        return ApiKey.SASL_AUTHENTICATE
