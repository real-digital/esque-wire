
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class DeleteGroupsRequestData(RequestData):
    """
    :param groups: An array of groups to be deleted.
    :type groups: List[str]
    """
    
    groups: List[str]

    @staticmethod
    def api_key() -> int:
        """
        :return: `42`, the api key for this API.
        """
        return ApiKey.DELETE_GROUPS

