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
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.SASL_AUTHENTICATE` (`ApiKey(36)`)
        """
        return ApiKey.SASL_AUTHENTICATE
