from .connection import BrokerConnection
from io import BytesIO
from typing import BinaryIO, Dict, Generic, Optional, TypeVar
from .structs.api_versions_response import ApiVersion
from .constants import ApiKey
from .serializers import REQUEST_SERIALIZERS, RESPONSE_SERIALIZERS
from .serializers.primitive import BaseSerializer
from .serializers.header import requestHeaderSerializer, responseHeaderSerializer
from .structs.header import RequestData, ResponseData, RequestHeader, ResponseHeader


SUPPORTED_API_VERSIONS: Dict[ApiKey, ApiVersion] = {
    api_key: ApiVersion(api_key, min(serializers.keys()), max(serializers.keys()))
    for api_key, serializers in REQUEST_SERIALIZERS.items()
}


def get_request_serializer(api_key: ApiKey, api_version: int) -> BaseSerializer[RequestData]:
    return REQUEST_SERIALIZERS[api_key][api_version]


def get_response_serializer(api_key: ApiKey, api_version: int) -> BaseSerializer[ResponseData]:
    return RESPONSE_SERIALIZERS[api_key][api_version]


Req = TypeVar("Req")
Res = TypeVar("Res")


class Request(Generic[Req, Res]):
    def __init__(self, request_data: Req, header: RequestHeader):
        self.api_version = header.api_version
        self.request_data = request_data
        self.request_header = header
        self.response_data: Optional[Res] = None
        self.response_header: Optional[ResponseHeader] = None

    def encode_request(self) -> bytes:
        data = requestHeaderSerializer.encode(self.request_header)
        data += self.request_serializer.encode(self.request_data)
        return data

    def decode_response(self, data: bytes) -> "Request":
        return self.read_response(BytesIO(data))

    def read_response(self, buffer: BinaryIO) -> "Request":
        self.response_header = responseHeaderSerializer.read(buffer)
        assert self.response_header.correlation_id == self.correlation_id, "Request and response order got messed up!"
        self.response_data = self.response_serializer.read(buffer)
        return self

    @property
    def correlation_id(self) -> int:
        return self.request_header.correlation_id

    @property
    def api_key(self) -> ApiKey:
        return self.request_header.api_key

    @property
    def response_serializer(self) -> BaseSerializer[Res]:
        return get_response_serializer(self.api_key, self.api_version)

    @property
    def request_serializer(self) -> BaseSerializer[Req]:
        return get_request_serializer(self.api_key, self.api_version)

    @classmethod
    def from_request_data(
        cls, request_data: Req, api_version: int, correlation_id: int, client_id: Optional[str]
    ) -> "Request":
        request_data = request_data
        header = RequestHeader(
            api_key=request_data.api_key(), api_version=api_version, correlation_id=correlation_id, client_id=client_id
        )
        return Request(request_data, header)