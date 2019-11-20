from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData


@dataclass
class AddOffsetsToTxnRequestData(RequestData):
    """
    :param transactional_id: The transactional id corresponding to the transaction.
    :type transactional_id: str
    :param producer_id: Current producer id in use by the transactional id.
    :type producer_id: int
    :param producer_epoch: Current epoch associated with the producer id.
    :type producer_epoch: int
    :param group_id: The unique group identifier
    :type group_id: str
    """

    transactional_id: str
    producer_id: int
    producer_epoch: int
    group_id: str

    @staticmethod
    def api_key() -> ApiKey:
        """
        :return: the api key for this API: `ApiKey.ADD_OFFSETS_TO_TXN` (`ApiKey(25)`)
        """
        return ApiKey.ADD_OFFSETS_TO_TXN
