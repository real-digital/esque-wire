from typing import List, Optional
from dataclasses import dataclass

from ...constants import ApiKey, ErrorCode
from ..base import ResponseData


@dataclass
class CreationResponse:
    """
    :param error_code: Response error code
    :type error_code: ErrorCode
    :param error_message: Response error message
    :type error_message: Optional[str]
    """

    error_code: ErrorCode
    error_message: Optional[str]


@dataclass
class CreateAclsResponseData(ResponseData):
    """
    :param throttle_time_ms: Duration in milliseconds for which the request was throttled due to quota violation (Zero
                             if the request did not violate any quota)
    :type throttle_time_ms: int
    :param creation_responses: None
    :type creation_responses: List[CreationResponse]
    """

    throttle_time_ms: int
    creation_responses: List[CreationResponse]

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.CREATE_ACLS` (`ApiKey(30)`)
        """
        return ApiKey.CREATE_ACLS
