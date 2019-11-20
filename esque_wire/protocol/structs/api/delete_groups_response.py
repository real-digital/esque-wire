from typing import List
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class GroupErrorCode:
    """
    :param group_id: The unique group identifier
    :type group_id: str
    :param error_code: Response error code
    :type error_code: ErrorCode
    """

    group_id: str
    error_code: ErrorCode


@dataclass
class DeleteGroupsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param group_error_codes: An array of per group error codes.
    :type group_error_codes: List[GroupErrorCode]
    """

    throttle_time_ms: int
    group_error_codes: List[GroupErrorCode]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.DELETE_GROUPS` (`ApiKey(42)`)
        """
        return ApiKey.DELETE_GROUPS
