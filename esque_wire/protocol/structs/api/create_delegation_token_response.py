from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Owner:
    """
    :param principal_type: principalType of the Kafka principal
    :type principal_type: str
    :param name: name of the Kafka principal
    :type name: str
    """

    principal_type: str
    name: str


@dataclass
class CreateDelegationTokenResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: int
    :param owner: token owner.
    :type owner: Owner
    :param issue_timestamp: timestamp (in msec) when this token was generated.
    :type issue_timestamp: int
    :param expiry_timestamp: timestamp (in msec) at which this token expires.
    :type expiry_timestamp: int
    :param max_timestamp: max life time of this token.
    :type max_timestamp: int
    :param token_id: UUID to ensure uniqueness.
    :type token_id: str
    :param hmac: HMAC of the delegation token.
    :type hmac: bytes
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    """

    error_code: int
    owner: Owner
    issue_timestamp: int
    expiry_timestamp: int
    max_timestamp: int
    token_id: str
    hmac: bytes
    throttle_time_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `38`, the api key for this API.
        """
        return ApiKey.CREATE_DELEGATION_TOKEN
