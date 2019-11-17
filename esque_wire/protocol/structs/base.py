from ..constants import ApiKey
from dataclasses import dataclass

@dataclass
class RequestData:
    @staticmethod
    def api_key() -> ApiKey:
        raise NotImplementedError()


@dataclass
class ResponseData:
    @staticmethod
    def api_key() -> ApiKey:
        raise NotImplementedError()