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
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.EXPIRE_DELEGATION_TOKEN` (`ApiKey(40)`)
        """
        return ApiKey.EXPIRE_DELEGATION_TOKEN
