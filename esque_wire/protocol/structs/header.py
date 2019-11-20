from dataclasses import dataclass
from typing import Optional

from ..constants import ApiKey


@dataclass
class RequestHeader:
    api_key: ApiKey
    api_version: int  # INT16
    correlation_id: int  # INT32
    client_id: Optional[str]


@dataclass
class ResponseHeader:
    correlation_id: int  # INT32
