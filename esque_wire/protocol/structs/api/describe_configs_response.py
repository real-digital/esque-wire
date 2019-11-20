from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode, ResourceType
from ..base import ResponseData


@dataclass
class ConfigSynonym:
    """
    :param config_name: None
    :type config_name: str
    :param config_value: None
    :type config_value: Optional[str]
    :param config_source: None
    :type config_source: int
    """

    config_name: str
    config_value: Optional[str]
    config_source: int


@dataclass
class ConfigEntry:
    """
    :param config_name: None
    :type config_name: str
    :param config_value: None
    :type config_value: Optional[str]
    :param read_only: None
    :type read_only: bool
    :param config_source: None
    :type config_source: int
    :param is_sensitive: None
    :type is_sensitive: bool
    :param config_synonyms: None
    :type config_synonyms: List[ConfigSynonym]
    """

    config_name: str
    config_value: Optional[str]
    read_only: bool
    config_source: int
    is_sensitive: bool
    config_synonyms: List[ConfigSynonym]


@dataclass
class Resource:
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param error_message: Response error message
    :type error_message: Optional[str]
    :param resource_type: None
    :type resource_type: ResourceType
    :param resource_name: None
    :type resource_name: str
    :param config_entries: None
    :type config_entries: List[ConfigEntry]
    """

    error_code: ErrorCode
    error_message: Optional[str]
    resource_type: ResourceType
    resource_name: str
    config_entries: List[ConfigEntry]


@dataclass
class DescribeConfigsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param resources: None
    :type resources: List[Resource]
    """

    throttle_time_ms: int
    resources: List[Resource]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DESCRIBE_CONFIGS` (`ApiKey(32)`)
        """
        return ApiKey.DESCRIBE_CONFIGS
