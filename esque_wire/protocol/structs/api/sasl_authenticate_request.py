
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class SaslAuthenticateRequestData(RequestData):
    """
    :param auth_bytes: The SASL authentication bytes from the client, as defined by the SASL mechanism.
    :type auth_bytes: bytes
    """
    
    auth_bytes: bytes

    @staticmethod
    def api_key() -> int:
        """
        :return: `36`, the api key for this API.
        """
        return ApiKey.SASL_AUTHENTICATE

