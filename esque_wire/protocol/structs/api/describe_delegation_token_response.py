from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class Renewer:
    """
    :param principal_type: principalType of the Kafka principal
    :type principal_type: str
    :param name: name of the Kafka principal
    :type name: str
    """

    principal_type: str
    name: str


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
class TokenDetail:
    """
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
    :param hmac: HMAC of the delegation token to be expired.
    :type hmac: bytes
    :param renewers: An array of token renewers. Renewer is an Kafka PrincipalType and name string, who is allowed to
                     renew this token before the max lifetime expires.
    :type renewers: List[Renewer]
    """

    owner: Owner
    issue_timestamp: int
    expiry_timestamp: int
    max_timestamp: int
    token_id: str
    hmac: bytes
    renewers: List[Renewer]


@dataclass
class DescribeDelegationTokenResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: int
    :param token_details: None
    :type token_details: List[TokenDetail]
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    """

    error_code: int
    token_details: List[TokenDetail]
    throttle_time_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `41`, the api key for this API.
        """
        return ApiKey.DESCRIBE_DELEGATION_TOKEN
