#!/usr/bin/env python3
import enum
import json
import pathlib
import sys
from typing import Any, Dict, Iterable, List, Set, Tuple, Optional

import inflection
import jinja2

if sys.version_info < (3, 6):
    raise RuntimeError("This script needs at least python3.6 to run.")

import dataclasses

API_INPUT_FILE = pathlib.Path(__file__).parent / "api_definition.json"
CONSTANTS_INPUT_FILE = pathlib.Path(__file__).parent / "constant_definition.json"
BASE_PATH = pathlib.Path(__file__).parent / "kafka_protocol"
TEMPLATE_PATH = BASE_PATH.parent / "templates"


class FieldType(str, enum.Enum):
    ARRAY = "ARRAY"
    STRUCT = "STRUCT"
    BOOLEAN = "BOOLEAN"
    INT8 = "INT8"
    INT16 = "INT16"
    INT32 = "INT32"
    INT64 = "INT64"
    UINT32 = "UINT32"
    VARINT = "VARINT"
    VARLONG = "VARLONG"
    STRING = "STRING"
    NULLABLE_STRING = "NULLABLE_STRING"
    BYTES = "BYTES"
    NULLABLE_BYTES = "NULLABLE_BYTES"
    RECORDS = "RECORDS"


class Direction(enum.Enum):
    REQUEST = "request"
    RESPONSE = "response"


def serializer(type_def: "TypeDef") -> str:
    assert type_def.field_type not in (FieldType.ARRAY, FieldType.STRUCT), "Should use their own implementation"
    return inflection.camelize(type_def.field_type.name, uppercase_first_letter=False) + "Serializer"


@dataclasses.dataclass
class TypeDef:
    field_type: FieldType

    def traverse_types(self) -> Iterable["TypeDef"]:
        yield self

    @staticmethod
    def from_dict(data: Dict) -> "TypeDef":
        field_type = FieldType(data["type"])
        if field_type == FieldType.ARRAY:
            return ArrayTypeDef.from_dict(data)
        if field_type == FieldType.STRUCT:
            return StructTypeDef.from_dict(data)
        return TypeDef(field_type)

    @property
    def type_hint(self) -> str:
        assert self.field_type not in (FieldType.ARRAY, FieldType.STRUCT), "Should use their own implementation"
        if self.field_type == FieldType.BOOLEAN:
            return "bool"
        elif self.field_type == FieldType.INT8:
            return "int"
        elif self.field_type == FieldType.INT16:
            return "int"
        elif self.field_type == FieldType.INT32:
            return "int"
        elif self.field_type == FieldType.INT64:
            return "int"
        elif self.field_type == FieldType.UINT32:
            return "int"
        elif self.field_type == FieldType.VARINT:
            return "int"
        elif self.field_type == FieldType.VARLONG:
            return "int"
        elif self.field_type == FieldType.STRING:
            return "str"
        elif self.field_type == FieldType.NULLABLE_STRING:
            return "Optional[str]"
        elif self.field_type == FieldType.BYTES:
            return "bytes"
        elif self.field_type == FieldType.NULLABLE_BYTES:
            return "Optional[bytes]"
        elif self.field_type == FieldType.RECORDS:
            return "Optional[bytes]"
        else:
            raise ValueError(f"No type hint for {self.field_type}")


@dataclasses.dataclass
class ArrayTypeDef(TypeDef):
    element_type: TypeDef

    @staticmethod
    def from_dict(data: Dict) -> "ArrayTypeDef":
        return ArrayTypeDef(FieldType.ARRAY, TypeDef.from_dict(data["element_type"]))

    def traverse_types(self) -> Iterable["TypeDef"]:
        yield self
        yield from self.element_type.traverse_types()

    @property
    def type_hint(self) -> str:
        return f"List[{self.element_type.type_hint}]"


@dataclasses.dataclass
class StructTypeDef(TypeDef):
    fields: List["Field"]
    name: str = "<noname>"
    field_names: List[str] = dataclasses.field(init=False, default_factory=list)

    @staticmethod
    def from_dict(data: Dict) -> "StructTypeDef":
        fields = [Field.from_dict(field_data) for field_data in data["fields"]]
        return StructTypeDef(FieldType.STRUCT, fields)

    def traverse_types(self) -> Iterable["TypeDef"]:
        yield self
        for field in self.fields:
            yield from field.type_def.traverse_types()

    def traverse_fields(self) -> Iterable["Field"]:
        for type_def in self.traverse_types():
            if isinstance(type_def, StructTypeDef):
                yield from type_def.fields

    @property
    def type_hint(self) -> str:
        return self.name


SEEN = set()


@dataclasses.dataclass
class Field:
    name: str
    doc: str
    default: Any
    has_default: bool
    type_def: TypeDef

    @classmethod
    def from_dict(cls, data: Dict) -> "Field":
        type_def = TypeDef.from_dict(data)
        return Field(data["name"], data["doc"], data["default"], data["has_default"], type_def)

    @property
    def type_hint(self) -> str:
        return self.type_def.type_hint


@dataclasses.dataclass
class ApiSchema:
    api_key: int
    api_version: int
    api_name: str
    direction: Direction
    schema: StructTypeDef
    structs: Dict[str, StructTypeDef] = dataclasses.field(default_factory=dict)
    structs_ordered: List[StructTypeDef] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self._assign_names_to_structs()
        self._create_struct_dict()
        self._resolve_struct_dependencies()

    def _assign_names_to_structs(self) -> None:
        self.schema.name = (
            inflection.camelize(self.api_name.lower(), uppercase_first_letter=True)
            + self.direction.name.title()
            + "Data"
        )
        for field, struct_type in self.find_struct_fields():
            struct_name = field.name
            if isinstance(field.type_def, ArrayTypeDef):
                struct_name = singularize(struct_name)
            struct_type.name = inflection.camelize(struct_name, uppercase_first_letter=True)

    def find_struct_fields(self) -> Iterable[Tuple[Field, StructTypeDef]]:
        for field in self.schema.traverse_fields():
            inner_type = skip_array_type_defs(field.type_def)
            if isinstance(inner_type, StructTypeDef):
                yield field, inner_type

    def _create_struct_dict(self):
        for _, struct in self.find_struct_fields():
            self.structs[struct.name] = struct
        self.structs[self.schema.name] = self.schema

    def _resolve_struct_dependencies(self):
        dependency_tree: Dict[str, Set[str]] = {}
        to_be_visited: List[StructTypeDef] = [self.schema]
        while to_be_visited:
            current_struct = to_be_visited.pop()
            dependency_tree[current_struct.name] = set()
            for field in current_struct.fields:
                inner_type = skip_array_type_defs(field.type_def)
                if isinstance(inner_type, StructTypeDef):
                    to_be_visited.append(inner_type)
                    dependency_tree[current_struct.name].add(inner_type.name)

        while dependency_tree:
            for name, dependencies in dependency_tree.items():
                if len(dependencies) == 0:
                    break
            else:
                raise RuntimeError("No Struct without dependencies found!")
            del dependency_tree[name]
            self.structs_ordered.append(self.structs[name])
            for dependencies in dependency_tree.values():
                dependencies.discard(name)


@dataclasses.dataclass
class Api:
    api_key: int
    api_name: str
    cluster_aciton: bool
    api_versions: Dict[int, Dict[Direction, ApiSchema]]
    latest_version: int = dataclasses.field(init=False)
    latest_schema_pair: Dict[Direction, ApiSchema] = dataclasses.field(init=False)
    min_supported_version: int = dataclasses.field(init=False)
    max_supported_version: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.latest_version = max(self.api_versions)
        self.max_supported_version = self.latest_version
        self.min_supported_version = min(self.api_versions)
        self.latest_schema_pair = self.api_versions[self.latest_version]

    @classmethod
    def from_dict(cls, data: Dict) -> "Api":
        api_key = data["api_key"]
        api_name = data["api_name"]
        schema_iterator: Iterable[Tuple[int, Tuple[Dict, Dict]]] = enumerate(
            zip(data["request_schemas"], data["response_schemas"])
        )
        api_versions: Dict[int, Dict[Direction, ApiSchema]] = {}
        for api_version, (request_schema, response_schema) in schema_iterator:
            schema_pair = {
                Direction.REQUEST: ApiSchema(
                    api_key, api_version, api_name, Direction.REQUEST, StructTypeDef.from_dict(request_schema)
                ),
                Direction.RESPONSE: ApiSchema(
                    api_key, api_version, api_name, Direction.RESPONSE, StructTypeDef.from_dict(response_schema)
                ),
            }
            api_versions[api_version] = schema_pair
        return Api(api_key, api_name, data["cluster_action"], api_versions)


def main():
    constants = load_constants(CONSTANTS_INPUT_FILE)
    api_data = load_api_data(API_INPUT_FILE)
    render(api_data, constants)


def load_constants(path: pathlib.Path) -> Dict:
    with path.open("r") as f:
        constants = json.load(f)
    return constants


def load_api_data(path: pathlib.Path) -> List[Api]:
    with path.open("r") as f:
        all_apis = json.load(f)
    return [Api.from_dict(data) for data in all_apis]


def skip_array_type_defs(type_def: TypeDef) -> TypeDef:
    while isinstance(type_def, ArrayTypeDef):
        type_def = type_def.element_type
    return type_def


def singularize(text: str) -> str:
    if text.endswith("data"):
        return text
    return inflection.singularize(text)


def lower_first(word: str) -> str:
    return word[0].lower() + word[1:]


PRIMITIVE_SERIALIZERS: Dict[FieldType, str] = {
    FieldType.BOOLEAN: "booleanSerializer",
    FieldType.INT8: "int8Serializer",
    FieldType.INT16: "int16Serializer",
    FieldType.INT32: "int32Serializer",
    FieldType.INT64: "int64Serializer",
    FieldType.UINT32: "uint32Serializer",
    FieldType.VARINT: "varIntSerializer",
    FieldType.VARLONG: "varLongSerializer",
    FieldType.STRING: "stringSerializer",
    FieldType.NULLABLE_STRING: "nullableStringSerializer",
    FieldType.BYTES: "bytesSerializer",
    FieldType.NULLABLE_BYTES: "nullableBytesSerializer",
    FieldType.RECORDS: "nullableBytesSerializer",
}


class Templater:
    template: jinja2.Template
    path_template: str
    last_target_path: Optional[pathlib.Path]

    def __init__(self, env: jinja2.Environment, template_path: pathlib.Path):
        self.template = env.get_template(str(template_path.relative_to(TEMPLATE_PATH)))
        path_template = str(BASE_PATH / template_path.relative_to(TEMPLATE_PATH))
        self.path_template = path_template.replace("<", "{").replace(">", "}")[:-3]
        self.last_target_path = None

    def render(self, all_apis: List[Api], current_api: Api, direction: Direction, constants: Dict):
        new_target_path = pathlib.Path(
            self.path_template.format(api_name=current_api.api_name.lower(), direction=direction.name.lower())
        )
        if new_target_path == self.last_target_path:
            return
        self.last_target_path = new_target_path
        new_target_path.parent.mkdir(parents=True, exist_ok=True)

        latest_schema = current_api.latest_schema_pair[direction]
        all_schemas = [api_schema[direction] for api_schema in current_api.api_versions.values()]
        new_target_path.write_text(
            self.template.render(
                all_apis=all_apis,
                current_api=current_api,
                latest_schema=latest_schema,
                all_schemas=all_schemas,
                direction=direction,
                constants=constants
            )
        )


def render(all_apis: List[Api], constants: Dict) -> None:
    loader = jinja2.FileSystemLoader(str(TEMPLATE_PATH))
    env = jinja2.Environment(autoescape=False, loader=loader)
    env.globals["Direction"] = Direction
    env.globals["FieldType"] = FieldType
    env.globals["len"] = len
    env.filters["lower_first"] = lower_first
    env.filters["repr"] = repr
    env.filters["primitive_serializer"] = PRIMITIVE_SERIALIZERS.get

    templaters = [
        Templater(env, path) for path in TEMPLATE_PATH.glob("**/*.py.j2") if path.name != "base_module.py.j2"
    ]

    for current_api in all_apis:
        for direction in Direction:
            for templater in templaters:
                templater.render(all_apis, current_api, direction, constants)


if __name__ == "__main__":
    main()
