from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey, ResourceType
from ..base import RequestData


@dataclass
class ConfigEntry:
    """
    :param config_name: Configuration name
    :type config_name: str
    :param config_value: Configuration value
    :type config_value: Optional[str]
    """

    config_name: str
    config_value: Optional[str]


@dataclass
class Resource:
    """
    :param resource_type: None
    :type resource_type: ResourceType
    :param resource_name: None
    :type resource_name: str
    :param config_entries: None
    :type config_entries: List[ConfigEntry]
    """

    resource_type: ResourceType
    resource_name: str
    config_entries: List[ConfigEntry]


@dataclass
class AlterConfigsRequestData(RequestData):
    """
    :param resources: An array of resources to update with the provided configs.
    :type resources: List[Resource]
    :param validate_only: None
    :type validate_only: bool
    """

    resources: List[Resource]
    validate_only: bool

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.ALTER_CONFIGS` (`ApiKey(33)`)
        """
        return ApiKey.ALTER_CONFIGS
