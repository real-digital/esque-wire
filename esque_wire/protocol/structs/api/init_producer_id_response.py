from dataclasses import dataclass

from ...constants import ApiKey
from ..base import ResponseData


@dataclass
class InitProducerIdResponseData(ResponseData):
    """
    :param throttle_time_ms: The duration in milliseconds for which the request was throttled due to a quota violation,
                             or zero if the request did not violate any quota.
    :type throttle_time_ms: int
    :param error_code: The error code, or 0 if there was no error.
    :type error_code: int
    :param producer_id: The current producer id.
    :type producer_id: int
    :param producer_epoch: The current epoch associated with the producer id.
    :type producer_epoch: int
    """

    throttle_time_ms: int
    error_code: int
    producer_id: int
    producer_epoch: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: `22`, the api key for this API.
        """
        return ApiKey.INIT_PRODUCER_ID