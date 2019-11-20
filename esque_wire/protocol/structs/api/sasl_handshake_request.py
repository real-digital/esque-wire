from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class SaslHandshakeRequestData(RequestData):
    """
    :param mechanism: The SASL mechanism chosen by the client.
    :type mechanism: str
    """

    mechanism: str

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.SASL_HANDSHAKE` (`ApiKey(17)`)
        """
        return ApiKey.SASL_HANDSHAKE
