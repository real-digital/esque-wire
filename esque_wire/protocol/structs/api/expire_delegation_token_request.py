
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class ExpireDelegationTokenRequestData(RequestData):
    """
    :param hmac: HMAC of the delegation token to be expired.
    :type hmac: bytes
    :param expiry_time_period: expiry time period in milli seconds.
    :type expiry_time_period: int
    """
    
    hmac: bytes
    expiry_time_period: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `40`, the api key for this API.
        """
        return ApiKey.EXPIRE_DELEGATION_TOKEN

