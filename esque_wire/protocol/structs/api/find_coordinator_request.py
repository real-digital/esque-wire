from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class FindCoordinatorRequestData(RequestData):
    """
    :param key: The coordinator key.
    :type key: str
    :param key_type: The coordinator key type.  (Group, transaction, etc.)
    :type key_type: int
    """

    key: str
    key_type: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.FIND_COORDINATOR` (`ApiKey(10)`)
        """
        return ApiKey.FIND_COORDINATOR
