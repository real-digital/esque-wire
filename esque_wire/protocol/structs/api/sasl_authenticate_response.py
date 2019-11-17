
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class SaslAuthenticateResponseData(ResponseData):
    """
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    :param error_message: The error message, or null if there was no error.
    :type error_message: Optional[str]
    :param auth_bytes: The SASL authentication bytes from the server, as defined by the SASL mechanism.
    :type auth_bytes: bytes
    :param session_lifetime_ms: The SASL authentication bytes from the server, as defined by the SASL mechanism.
    :type session_lifetime_ms: int
    """
    
    error_code: int
    error_message: Optional[str]
    auth_bytes: bytes
    session_lifetime_ms: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `36`, the api key for this API.
        """
        return ApiKey.SASL_AUTHENTICATE

