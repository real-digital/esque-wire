
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class Config:
    """
    :param name: The configuration key name.
    :type name: str
    :param config_operation: The type (Set, Delete, Append, Subtract) of operation.
    :type config_operation: int
    :param value: The value to set for the configuration key.
    :type value: Optional[str]
    """
    
    name: str
    config_operation: int
    value: Optional[str]


@dataclass
class Resource:
    """
    :param resource_type: The resource type.
    :type resource_type: int
    :param resource_name: The resource name.
    :type resource_name: str
    :param configs: The configurations.
    :type configs: List[Config]
    """
    
    resource_type: int
    resource_name: str
    configs: List[Config]


@dataclass
class IncrementalAlterConfigsRequestData(RequestData):
    """
    :param resources: The incremental updates for each resource.
    :type resources: List[Resource]
    :param validate_only: True if we should validate the request, but not change the configurations.
    :type validate_only: bool
    """
    
    resources: List[Resource]
    validate_only: bool

    @staticmethod
    def api_key() -> int:
        """
        :return: `44`, the api key for this API.
        """
        return ApiKey.INCREMENTAL_ALTER_CONFIGS

