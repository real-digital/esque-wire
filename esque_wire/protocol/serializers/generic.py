from enum import Enum
from typing import BinaryIO, Dict, Tuple, List, Type, TypeVar, Optional

from .base import BaseSerializer
from .primitive import int32Serializer

T = TypeVar("T")
Schema = List[Tuple[Optional[str], "BaseSerializer"]]


class DictSerializer(BaseSerializer[Dict]):
    def __init__(self, schema: Schema):
        self._schema = schema.copy()

    def encode(self, value: Dict) -> bytes:
        return b"".join(
            serializer.encode(value[field]) for field, serializer in self._schema
        )

    def read(self, buffer: BinaryIO) -> Dict:
        data = {}
        for field, serializer in self._schema:
            data[field] = serializer.read(buffer)
        return data

    @property
    def default(self) -> Dict:
        return {}


class ArraySerializer(BaseSerializer[T]):
    def __init__(self, elem_serializer: BaseSerializer[T]):
        self._elem_serializer: BaseSerializer[T] = elem_serializer

    def encode(self, elems: Optional[List[T]]) -> bytes:
        if elems is None:
            return int32Serializer.encode(-1)
        return int32Serializer.encode(len(elems)) + b"".join(
            self._elem_serializer.encode(elem) for elem in elems
        )

    def read(self, buffer: BinaryIO) -> Optional[List[T]]:
        len_ = int32Serializer.read(buffer)
        if len_ == -1:
            return None
        return [self._elem_serializer.read(buffer) for _ in range(len_)]

    @property
    def default(self) -> List:
        return []


class DataClassSerializer(BaseSerializer[T]):
    def __init__(self, data_class: Type[T], schema: Schema):
        self._schema = schema.copy()
        self.data_class: Type[T] = data_class

    def encode(self, value: T) -> bytes:
        return b"".join(
            serializer.encode(getattr(value, field))
            for field, serializer in self._schema
        )

    def read(self, buffer: BinaryIO) -> T:
        data = {}
        for field, serializer in self._schema:
            if field is None:
                # None fields are legacy, they're present and have
                # to be read but are not part of the data structure anymore
                serializer.read(buffer)
            else:
                data[field] = serializer.read(buffer)
        return self.data_class(**data)

    @property
    def default(self) -> T:
        return self.data_class(
            **{
                field: serializer.default
                for field, serializer in self._schema
                if field is not None
            }
        )


E = TypeVar("E", bound=Enum)


class EnumSerializer(BaseSerializer[E]):
    def __init__(self, enum_class: Type[E], serializer: BaseSerializer):
        self.enum_class = enum_class
        self.serializer = serializer

    def encode(self, value: E) -> bytes:
        return self.serializer.encode(value.value)

    def read(self, buffer: BinaryIO) -> E:
        return self.enum_class(self.serializer.read(buffer))

    @property
    def default(self) -> E:
        for member in self.enum_class:
            return member
        raise RuntimeError(
            f"Cannot dermine default, Enum {self.enum_class.__name__} is empty!"
        )


class DummySerializer(BaseSerializer[T]):
    def __init__(self, value: T):
        self.value = value

    def encode(self, value: T) -> bytes:
        return b""

    def read(self, buffer: BinaryIO) -> T:
        return self.value

    @property
    def default(self) -> T:
        return self.value
