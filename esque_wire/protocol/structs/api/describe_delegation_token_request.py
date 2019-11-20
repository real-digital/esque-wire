from typing import List
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


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
class DescribeDelegationTokenRequestData(RequestData):
    """
    :param owners: An array of token owners.
    :type owners: List[Owner]
    """

    owners: List[Owner]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DESCRIBE_DELEGATION_TOKEN` (`ApiKey(41)`)
        """
        return ApiKey.DESCRIBE_DELEGATION_TOKEN
