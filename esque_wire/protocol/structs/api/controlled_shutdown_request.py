from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class ControlledShutdownRequestData(RequestData):
    """
    :param broker_id: The id of the broker for which controlled shutdown has been requested.
    :type broker_id: int
    :param broker_epoch: The broker epoch.
    :type broker_epoch: int
    """

    broker_id: int
    broker_epoch: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.CONTROLLED_SHUTDOWN` (`ApiKey(7)`)
        """
        return ApiKey.CONTROLLED_SHUTDOWN
