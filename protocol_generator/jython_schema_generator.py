# Note: This file is meant to be run with Jython2.7
# Use generate_api_definition.py to do that for you

import json
import os
from collections import OrderedDict
from org.apache.kafka.common.protocol import ApiKeys
from org.apache.kafka.common.protocol.types import Type, Schema, ArrayOf


def main():
    api_definition = [
        api_key_to_dict(api_key) for api_key in ApiKeys.values()
    ]
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, "api_definition.json")
    with open(path, 'w') as o:
        json.dump(api_definition, o, indent=2)


def api_key_to_dict(api_key):
    api_dict = OrderedDict()
    api_dict["api_key"] = api_key.id
    api_dict["api_name"] = str(api_key)
    api_dict["request_schemas"] = [resolve_schema(schema) for schema in api_key.requestSchemas]
    api_dict["response_schemas"] = [resolve_schema(schema) for schema in api_key.responseSchemas]
    return api_dict


def resolve_schema(schema):
    schema_fields = OrderedDict()
    for field in map(get_def, schema.fields()):
        schema_fields[field.name] = resolve_field(field)
    return schema_fields

def get_def(bound_field):
    return bound_field.def


def resolve_field(field):
    field_dict = OrderedDict()
    field_dict["name"] = field.name
    field_dict["doc"] = field.docString
    field_dict["default"] = field.defaultValue
    field_dict["has_default"] = field.hasDefaultValue
    append_type_data(field_dict, field.type)
    return field_dict


def append_type_data(field_dict, type_):
    if isinstance(type_, Schema):
        field_dict["type"] = "struct"
        field_dict["fields"] = resolve_schema(type_)
    elif isinstance(type_, ArrayOf):
        field_dict["type"] = "array"
        type_dict = OrderedDict()
        append_type_data(type_dict, type_.type())
        field_dict["element_type"] = type_dict
    elif isinstance(type_, Type.DocumentedType):
        field_dict["type"] = type_.typeName()
    else:
        raise ValueError("Unkown type %s" % type_)


if __name__ == '__main__':
    main()

