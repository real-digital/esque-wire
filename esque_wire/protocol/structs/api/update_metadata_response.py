from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class UpdateMetadataResponseData(ResponseData):
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    """

    error_code: ErrorCode

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.UPDATE_METADATA` (`ApiKey(6)`)
        """
        return ApiKey.UPDATE_METADATA
