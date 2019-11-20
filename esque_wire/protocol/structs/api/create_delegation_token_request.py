from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


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
class CreateDelegationTokenRequestData(RequestData):
    """
    :param renewers: An array of token renewers. Renewer is an Kafka PrincipalType and name string, who is allowed to
                     renew this token before the max lifetime expires.
    :type renewers: List[Renewer]
    :param max_life_time: Max lifetime period for token in milli seconds. if value is -1, then max lifetime  will
                          default to a server side config value.
    :type max_life_time: int
    """

    renewers: List[Renewer]
    max_life_time: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.CREATE_DELEGATION_TOKEN` (`ApiKey(38)`)
        """
        return ApiKey.CREATE_DELEGATION_TOKEN
