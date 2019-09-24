from typing import BinaryIO, Dict, Generic, List, Type, TypeVar, Optional

from esque_wire.protocol.serializers.primitive import BaseSerializer, Schema, int16Serializer, int32Serializer

T = TypeVar("T")


class DictSerializer(BaseSerializer):
    def __init__(self, schema: Schema):
        self._schema = schema.copy()

    def encode(self, value: Dict) -> bytes:
        return b"".join(serializer.encode(value[field]) for field, serializer in self._schema)

    def read(self, buffer: BinaryIO) -> Dict:
        data = {}
        for field, serializer in self._schema:
            data[field] = serializer.read(buffer)
        return data


class ArraySerializer(BaseSerializer):
    def __init__(self, elem_serializer: BaseSerializer[T]):
        self._elem_serializer: BaseSerializer[T] = elem_serializer

    def encode(self, elems: Optional[List[T]]) -> bytes:
        if elems is None:
            return int32Serializer.encode(-1)
        return int32Serializer.encode(len(elems)) + b"".join(self._elem_serializer.encode(elem) for elem in elems)

    def read(self, buffer: BinaryIO) -> Optional[List[T]]:
        len_ = int32Serializer.read(buffer)
        if len_ == -1:
            return None
        return [self._elem_serializer.read(buffer) for _ in range(len_)]


# TODO: figure out how to properly bind T to NamedTuple, doesn't seem to work with an additional
#  TypeVar(..., bound=NamedTuple)
class NamedTupleSerializer(DictSerializer):
    def __init__(self, tuple_class: Type[T], schema: Schema):
        super().__init__(schema)
        self.tuple_class = tuple_class

    def encode(self, value: T) -> bytes:
        return b"".join(serializer.encode(getattr(value, field)) for field, serializer in self._schema)

    def read(self, buffer: BinaryIO) -> T:
        data = super().read(buffer)
        data.pop(None, None)  # None fields are supposed to be ignored, pop the field if one is there
        return self.tuple_class(**data)


# TODO: see above
class EnumSerializer(BaseSerializer):
    def __init__(self, enum_class: Type[T], serializer: BaseSerializer):
        self.enum_class = enum_class
        self.serializer = serializer

    def encode(self, value: T) -> bytes:
        return self.serializer.encode(value.value)

    def read(self, buffer: BinaryIO) -> T:
        return self.enum_class(self.serializer.read(buffer))


class DummySerializer(BaseSerializer):
    def __init__(self, value: T):
        self.value = value

    def encode(self, value: T) -> bytes:
        return b""

    def read(self, buffer: BinaryIO) -> T:
        return self.value
