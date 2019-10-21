# Note: This file is meant to be run with Jython2.7

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
    api_dict["request_schemas"] = [get_fields_from_schema(schema) for schema in api_key.requestSchemas]
    api_dict["response_schemas"] = [get_fields_from_schema(schema) for schema in api_key.responseSchemas]
    return api_dict

def get_fields_from_schema(schema):
    schema_fields = []
    for field in map(get_def, schema.fields()):
        field_dict = OrderedDict()
        field_dict["name"] = field.name
        field_dict["doc"] = field.docString
        append_type_data(field_dict, field.type)
        schema_fields.append(field_dict)
    return schema_fields


def get_def(bound_field):
    return bound_field.def


def append_type_data(field_dict, type_):
    if isinstance(type_, Schema):
        field_dict["type"] = "struct"
        field_dict["fields"] = get_fields_from_schema(type_)
    elif isinstance(type_, ArrayOf):
        field_dict["type"] = "array"
        type_dict = OrderedDict()
        append_type_data(type_dict, type_.type())
        field_dict["element_type"] = type_dict
    elif isinstance(type_, Type.DocumentedType):
        field_dict["type"] = "primitive"
        field_dict["primitive_type"] = type_.typeName()
    else:
        raise ValueError("Unkown type %s" % type_)


if __name__ == '__main__':
    main()

