from .generic import Schema, DataClassSerializer
from .constants import apiKeySerializer
from .primitive import int16Serializer, int32Serializer, nullableStringSerializer
from ..structs.header import RequestHeader, ResponseHeader

requestHeaderSchema: Schema = [
    ("api_key", apiKeySerializer),
    ("api_version", int16Serializer),
    ("correlation_id", int32Serializer),
    ("client_id", nullableStringSerializer),
]

requestHeaderSerializer = DataClassSerializer(RequestHeader, requestHeaderSchema)

responseHeaderSchema: Schema = [("correlation_id", int32Serializer)]

responseHeaderSerializer = DataClassSerializer(ResponseHeader, responseHeaderSchema)
