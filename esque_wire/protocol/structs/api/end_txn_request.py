
from typing import Dict, List, Optional

from dataclasses import dataclass

from ...constants import ApiKey
from ..base import RequestData





@dataclass
class EndTxnRequestData(RequestData):
    """
    :param transactional_id: The transactional id corresponding to the transaction.
    :type transactional_id: str
    :param producer_id: Current producer id in use by the transactional id.
    :type producer_id: int
    :param producer_epoch: Current epoch associated with the producer id.
    :type producer_epoch: int
    :param transaction_result: The result of the transaction (0 = ABORT, 1 = COMMIT)
    :type transaction_result: bool
    """
    
    transactional_id: str
    producer_id: int
    producer_epoch: int
    transaction_result: bool

    @staticmethod
    def api_key() -> int:
        """
        :return: `26`, the api key for this API.
        """
        return ApiKey.END_TXN

