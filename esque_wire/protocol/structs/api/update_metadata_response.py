
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData





@dataclass
class UpdateMetadataResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: int
    """
    
    error_code: int

    @staticmethod
    def api_key() -> int:
        """
        :return: `6`, the api key for this API.
        """
        return ApiKey.UPDATE_METADATA

