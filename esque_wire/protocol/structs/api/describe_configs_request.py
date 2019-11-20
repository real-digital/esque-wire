from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ResourceType
from ..base import RequestData


@dataclass
class Resource:
    """
    :param resource_type: None
    :type resource_type: ResourceType
    :param resource_name: None
    :type resource_name: str
    :param config_names: None
    :type config_names: List[str]
    """

    resource_type: ResourceType
    resource_name: str
    config_names: List[str]


@dataclass
class DescribeConfigsRequestData(RequestData):
    """
    :param resources: An array of config resources to be returned.
    :type resources: List[Resource]
    :param include_synonyms: None
    :type include_synonyms: bool
    """

    resources: List[Resource]
    include_synonyms: bool

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DESCRIBE_CONFIGS` (`ApiKey(32)`)
        """
        return ApiKey.DESCRIBE_CONFIGS
