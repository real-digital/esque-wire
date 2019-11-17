
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class RenewDelegationTokenRequestData(RequestData):
    """
    :param hmac: HMAC of the delegation token to be renewed.
    :type hmac: bytes
    :param renew_time_period: Renew time period in milli seconds.
    :type renew_time_period: int
    """
    
    hmac: bytes
    renew_time_period: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `39`, the api key for this API.
        """
        return ApiKey.RENEW_DELEGATION_TOKEN

