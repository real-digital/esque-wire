from typing import Optional
from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class InitProducerIdRequestData(RequestData):
    """
    :param transactional_id: The transactional id, or null if the producer is not transactional.
    :type transactional_id: Optional[str]
    :param transaction_timeout_ms: The time in ms to wait for before aborting idle transactions sent by this producer.
                                   This is only relevant if a TransactionalId has been defined.
    :type transaction_timeout_ms: int
    """

    transactional_id: Optional[str]
    transaction_timeout_ms: int

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.INIT_PRODUCER_ID` (`ApiKey(22)`)
        """
        return ApiKey.INIT_PRODUCER_ID
