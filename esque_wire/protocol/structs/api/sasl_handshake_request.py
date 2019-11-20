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
        :return: `17`, the api key for this API.
        """
        return ApiKey.SASL_HANDSHAKE
