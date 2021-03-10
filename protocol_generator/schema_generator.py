#!/usr/bin/env python3
import dataclasses
import enum
import json
import pathlib
import subprocess
import textwrap
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, TypeVar

import inflection
import jinja2
from jinja2 import StrictUndefined

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

API_INPUT_FILE = PROJECT_ROOT / "protocol_generator" / "api_definition.json"
CONSTANTS_INPUT_FILE = PROJECT_ROOT / "protocol_generator" / "constant_definition.json"
TARGET_PATH = PROJECT_ROOT / "esque_wire"
TEMPLATE_PATH = PROJECT_ROOT / "protocol_generator" / "templates"
T = TypeVar("T")


class FieldType(str, enum.Enum):
    ARRAY = "ARRAY"
    STRUCT = "STRUCT"
    BOOLEAN = "BOOLEAN"
    ENUM = "ENUM"
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
        if field_type == FieldType.ENUM:
            return EnumTypeDef.from_dict(data)
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

    @property
    def type_import_name(self) -> Optional[str]:
        if self.field_type in (FieldType.NULLABLE_BYTES, FieldType.NULLABLE_STRING, FieldType.RECORDS):
            return "Optional"
        return None

    @property
    def serializer_import_name(self) -> str:
        return PRIMITIVE_SERIALIZERS[self.field_type]

    @property
    def constant_import_name(self) -> Optional[str]:
        return None

    def serializer_definition(self, version=0):
        return PRIMITIVE_SERIALIZERS[self.field_type]

    def serializer_variable_name(self, version=0):
        return PRIMITIVE_SERIALIZERS[self.field_type]


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

    @property
    def type_import_name(self) -> Optional[str]:
        return "List"

    @property
    def serializer_import_name(self) -> str:
        return "ArraySerializer"

    def serializer_definition(self, version=0):
        return f"ArraySerializer({self.element_type.serializer_definition(version)})"

    def serializer_variable_name(self, version=0):
        return f"ArraySerializer({self.element_type.serializer_variable_name(version)})"


@dataclasses.dataclass
class DummyTypeDef(TypeDef):
    element_type: TypeDef
    default: Any
    has_default: bool

    def traverse_types(self) -> Iterable["TypeDef"]:
        yield self
        yield from self.element_type.traverse_types()

    @property
    def type_hint(self) -> str:
        return self.element_type.type_hint

    @property
    def serializer_import_name(self) -> str:
        return "DummySerializer"

    def serializer_definition(self, version=0):
        if self.has_default:
            default_def = repr(self.default)
        else:
            default_def = self.element_type.serializer_definition()
            default_def += ".default"
        return f"DummySerializer({default_def})"

    def serializer_variable_name(self, version=0):
        if self.has_default:
            default_def = repr(self.default)
        else:
            default_def = self.element_type.serializer_variable_name(-1)
            default_def += ".default"
        return f"DummySerializer({default_def})"


@dataclasses.dataclass
class StructTypeDef(TypeDef):
    fields: List["Field"]
    name: str = "<noname>"
    field_names: List[str] = dataclasses.field(init=False, default_factory=list)

    def __post_init__(self):
        self.field_names.extend(f.name for f in self.fields)

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

    def schema_dict_name(self, include_type: bool = False) -> str:
        name = f"{lower_first(self.name)}Schemas"
        if include_type:
            name += ": Dict[int, Schema]"
        return name

    def schema_variable_name(self, version: int = 0) -> str:
        return f"{self.schema_dict_name()}[{version}]"

    def serializer_dict_name(self, include_type: bool = False) -> str:
        name = f"{ lower_first(self.name) }Serializers"
        if include_type:
            name += f": Dict[int, ClassSerializer[{self.name}]]"
        return name

    def serializer_variable_name(self, version: int = 0) -> str:
        return f"{self.serializer_dict_name()}[{version}]"

    @property
    def serializer_import_name(self) -> str:
        return "ClassSerializer"

    def serializer_definition(self, version: int = 0, schema: Optional[str] = None) -> str:
        if schema is None:
            schema = self.schema_variable_name(version)
        return f"ClassSerializer({self.name}, {schema})"

    def make_compatible_to(self, other_struct: "StructTypeDef") -> None:
        self._skip_extra_fields(other_struct)
        self._add_missing_fields(other_struct)

    def _skip_extra_fields(self, other_struct: "StructTypeDef") -> None:
        for field in self.fields:
            if field.name not in other_struct.field_names:
                field.skip = True

    def _add_missing_fields(self, other_struct: "StructTypeDef") -> None:
        for field in other_struct.fields:
            if field.name not in self.field_names:
                dummy_type = DummyTypeDef(
                    field_type=field.type_def.field_type,
                    element_type=field.type_def,
                    default=field.default,
                    has_default=field.has_default,
                )
                dummy_field = dataclasses.replace(field, type_def=dummy_type)
                self.fields.append(dummy_field)
                self.field_names.append(field.name)


@dataclasses.dataclass
class EnumTypeDef(TypeDef):
    enum_class: str
    # Maybe we'll have to keep the primitive type here (i.e. INT8 or INT16) and create a custom serializer
    # when the data type is non-default, but I hope that they're always the same for the same enum class.
    # We define the default types in jython_api_gen.py in order to create the enum serializers in
    # serializers/constants.py

    @staticmethod
    def from_dict(data: Dict) -> "EnumTypeDef":
        return EnumTypeDef(FieldType.ARRAY, enum_class=data["enum_class"])

    @property
    def type_hint(self) -> str:
        return self.enum_class

    @property
    def struct_import_name(self) -> Optional[str]:
        return self.enum_class

    @property
    def serializer_import_name(self) -> str:
        return lower_first(self.enum_class) + "Serializer"

    def serializer_definition(self, version=0):
        return self.serializer_import_name

    def serializer_variable_name(self, version=0):
        return self.serializer_import_name

    @property
    def constant_import_name(self) -> Optional[str]:
        return self.enum_class


@dataclasses.dataclass
class Field:
    name: str
    doc: str
    default: Any
    has_default: bool
    type_def: TypeDef
    skip: bool = False

    @classmethod
    def from_dict(cls, data: Dict) -> "Field":
        type_def = TypeDef.from_dict(data)
        return Field(data["name"], data["doc"], data["default"], data["has_default"], type_def)

    @property
    def type_hint(self) -> str:
        return self.type_def.type_hint

    @property
    def rendered_name(self) -> str:
        if self.skip:
            return "None"
        return repr(self.name)


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

    def make_compatible_to(self, other_schema: "ApiSchema") -> None:
        for struct_name, other_struct in other_schema.structs.items():
            if struct_name in self.structs:
                self.structs[struct_name].make_compatible_to(other_struct)


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
        self._make_old_structs_compatible()

    def _make_old_structs_compatible(self) -> None:
        for direction in Direction:
            new_schema = self.latest_schema_pair[direction]
            for api_version, old_schema_pair in self.api_versions.items():
                if api_version == self.latest_version:
                    continue
                old_schema = old_schema_pair[direction]
                old_schema.make_compatible_to(new_schema)

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

    def get_serializer_imports(self, direction: Direction) -> List[str]:
        serializers = {"Schema"}
        for version_pair in self.api_versions.values():
            schema = version_pair[direction]
            for field_type in schema.schema.traverse_types():
                name = field_type.serializer_import_name
                if name is not None:
                    serializers.add(name)
        return sorted(serializers - {None})

    def get_type_imports(self, direction: Direction) -> List[str]:
        type_hints = {"ClassVar"}
        for version_pair in self.api_versions.values():
            schema = version_pair[direction]
            for field_type in schema.schema.traverse_types():
                name = field_type.type_import_name
                if name is not None:
                    type_hints.add(name)
        return sorted(type_hints - {None})

    def get_constant_imports(self, direction: Direction) -> List[str]:
        constants = {"ApiKey"}
        for version_pair in self.api_versions.values():
            schema = version_pair[direction]
            for field_type in schema.schema.traverse_types():
                name = field_type.constant_import_name
                if name is not None:
                    constants.add(name)
        return sorted(constants - {None})


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
    current_target_path: Optional[pathlib.Path]

    def __init__(self, env: jinja2.Environment, template_path: pathlib.Path):
        self.template = env.get_template(str(template_path.relative_to(TEMPLATE_PATH)))
        path_template = str(TARGET_PATH / template_path.relative_to(TEMPLATE_PATH))
        self.path_template = path_template.replace("<", "{").replace(">", "}")[:-3]
        self.last_target_path = None

    def render(self, all_apis: List[Api], current_api: Api, direction: Direction, constants: Dict) -> None:
        self._determine_target_path(current_api, direction)
        if not self._target_changed:
            return
        if self.current_target_path is None:
            raise RuntimeError("Need to determine target path first!")
        self._update_last_path()
        self.current_target_path.parent.mkdir(parents=True, exist_ok=True)

        latest_schema = current_api.latest_schema_pair[direction]
        all_versions = [api_schema[direction] for api_schema in current_api.api_versions.values()]
        self.current_target_path.write_text(
            self.template.render(
                all_apis=all_apis,
                current_api=current_api,
                latest_schema=latest_schema,
                all_versions=all_versions,
                direction=direction,
                constants=constants,
            )
        )

    def _determine_target_path(self, current_api: Api, direction: Direction) -> None:
        self.current_target_path = pathlib.Path(
            self.path_template.format(api_name=current_api.api_name.lower(), direction=direction.name.lower())
        )

    @property
    def _target_changed(self) -> bool:
        return self.current_target_path != self.last_target_path

    def _update_last_path(self) -> None:
        self.last_target_path = self.current_target_path


def without(seq: Iterable[T], *excluded_elems: T) -> Iterable[T]:
    for elem in seq:
        if elem not in excluded_elems:
            yield elem


def is_string(value: Any) -> bool:
    return isinstance(value, str)


def render_long_text(text: str, wrap_at: int = 100, **kwargs: Any) -> str:
    text = text.strip()
    if text == "":
        return '""'
    if len(text) < wrap_at:
        return repr(text)
    segments = textwrap.wrap(text, **kwargs)
    if len(segments) == 1:
        return repr(segments[0])
    joined = " ".join(map(repr, segments))
    return f"({joined})"


def render(all_apis: List[Api], constants: Dict) -> None:
    loader = jinja2.FileSystemLoader(str(TEMPLATE_PATH))
    env = jinja2.Environment(autoescape=False, loader=loader, undefined=StrictUndefined)
    env.globals["Direction"] = Direction
    env.globals["FieldType"] = FieldType
    env.globals["len"] = len
    env.filters["camelize"] = set
    env.filters["is_string"] = is_string
    env.filters["lower_first"] = lower_first
    env.filters["repr"] = repr
    env.filters["without"] = without
    env.filters["primitive_serializer"] = PRIMITIVE_SERIALIZERS.get
    env.filters["camelize"] = inflection.camelize
    env.filters["underscore"] = inflection.underscore
    env.filters["render_long_text"] = render_long_text
    env.filters["wrap"] = textwrap.wrap

    templaters = [
        Templater(env, path) for path in TEMPLATE_PATH.glob("**/*.py.j2") if path.name != "base_module.py.j2"
    ]

    for current_api in all_apis:
        for direction in Direction:
            for templater in templaters:
                templater.render(all_apis, current_api, direction, constants)

    run_isort()
    run_black()


def run_isort():
    subprocess.check_call(["isort", "-rc", str(TARGET_PATH)], cwd=str(PROJECT_ROOT))


def run_black():
    subprocess.check_call(["black", str(TARGET_PATH)], cwd=str(PROJECT_ROOT))


if __name__ == "__main__":
    main()
