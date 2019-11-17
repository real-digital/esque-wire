
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class SaslHandshakeResponseData(ResponseData):
    """
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    :param mechanisms: The mechanisms enabled in the server.
    :type mechanisms: List[str]
    """
    
    error_code: int
    mechanisms: List[str]

    @staticmethod
    def api_key() -> int:
        """
        :return: `17`, the api key for this API.
        """
        return ApiKey.SASL_HANDSHAKE

