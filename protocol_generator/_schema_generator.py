# Note: This file is meant to be run with Jython2.7

import json
import os
from collections import OrderedDict
from org.apache.kafka.common.protocol import ApiKeys
from org.apache.kafka.common.protocol.types import Type, Schema, ArrayOf


def main():
    dir = os.path.dirname(os.path.abspath(__file__))
    base_by_key = os.path.join(
                    dir,
                    'kafka_apis',
                    'by_key')
    base_by_name = os.path.join(
        dir,'kafka_apis','by_name'
    )
    try:
        os.makedirs(base_by_name)
    except OSError:
        pass

    api_keys = list(ApiKeys.values())
    for i, api_key in enumerate(api_keys, 1):
        print("Processing api {} {:2}/{:2}".format(str(api_key), i, len(api_keys)))
        definition = api_key_to_dict(api_key)
        for api_version, directions in definition["api_versions"].items():
            for direction, schema in directions.items():
                path = os.path.join(
                    base_by_key,
                    str(definition["api_key"]),
                    "v"+str(api_version),
                    direction)
                try:
                    os.makedirs(path)
                except OSError:
                    pass
                with open(os.path.join(path, "schema.json"), 'w') as o:
                    json.dump(schema, o, indent=2)
        os.symlink(
            os.path.join('..', 'by_key', str(definition["api_key"])),
            os.path.join(base_by_name, definition["api_name"].lower())
        )

def api_key_to_dict(api_key):
    api_dict = OrderedDict()
    api_dict["api_key"] = api_key.id
    api_dict["api_name"] = str(api_key)
    api_dict["api_versions"] = {
        i: {
            "request": append_type_data(OrderedDict(), req_schema),
            "response": append_type_data(OrderedDict(), res_schema)
        }
        for i, (req_schema, res_schema) in enumerate(zip(api_key.requestSchemas, api_key.responseSchemas))
    }
    return api_dict


def get_fields_from_schema(schema):
    schema_fields = OrderedDict()
    for field in map(get_def, schema.fields()):
        schema_fields[field.name] = create_field_dict(field)
    return schema_fields


def create_field_dict(field):
    field_dict = OrderedDict()
    if field.docString is not None:
        field_dict["description"] = field.docString
    if field.hasDefaultValue:
        field_dict["default"] = field.defaultValue
    append_type_data(field_dict, field.type)
    return field_dict


def get_def(bound_field):
    return bound_field.def


def append_type_data(field_dict, type_):
    if isinstance(type_, Schema):
        field_dict["type"] = "object"
        field_dict["properties"] = get_fields_from_schema(type_)
        field_dict["additionalProperties"] = False
        field_dict["requiredProperties"] = [
            field_name for field_name, field_def in field_dict["properties"].items()
            if "default" not in field_def
        ]
    elif isinstance(type_, ArrayOf):
        field_dict["type"] = "array"
        type_dict = OrderedDict()
        append_type_data(type_dict, type_.type())
        field_dict["items"] = type_dict
    elif isinstance(type_, Type.DocumentedType):
        append_primitive_type_data(field_dict, type_)
    else:
        raise ValueError("Unkown type %s" % type_)
    return field_dict

def append_primitive_type_data(field_dict, type_):
    name = type_.typeName()

    if name == "BOOLEAN":
        field_dict["kafka_type"] = "BOOLEAN"
        field_dict["type"] = "boolean"
    elif name == "INT8":
        field_dict["kafka_type"] = "INT8"
        field_dict["type"] = "integer"
        field_dict["minimum"] = -(2**7)
        field_dict["maximum"] = 2**7-1
    elif name == "INT16":
        field_dict["kafka_type"] = "INT16"
        field_dict["type"] = "integer"
        field_dict["minimum"] = -(2**15)
        field_dict["maximum"] = 2**15-1
    elif name == "INT32":
        field_dict["kafka_type"] = "INT32"
        field_dict["type"] = "integer"
        field_dict["minimum"] = -(2**31)
        field_dict["maximum"] = 2**31-1
    elif name == "INT64":
        field_dict["kafka_type"] = "INT64"
        field_dict["type"] = "integer"
        field_dict["minimum"] = -(2**63)
        field_dict["maximum"] = 2**63-1
    elif name == "UINT32":
        field_dict["kafka_type"] = "UINT32"
        field_dict["type"] = "integer"
        field_dict["minimum"] = 0
        field_dict["maximum"] = 2**32-1
    elif name == "VARINT":
        field_dict["kafka_type"] = "VARINT"
        field_dict["type"] = "integer"
        field_dict["minimum"] = -(2**31)
        field_dict["maximum"] = 2**31-1
    elif name == "VARLONG":
        field_dict["kafka_type"] = "VARLONG"
        field_dict["type"] = "integer"
        field_dict["minimum"] = -(2**63)
        field_dict["maximum"] = 2**63-1
    elif name == "STRING":
        field_dict["kafka_type"] = "STRING"
        field_dict["type"] = "string"
    elif name == "NULLABLE_STRING":
        field_dict["kafka_type"] = "NULLABLE_STRING"
        field_dict["type"] = ["string", "null"]
    elif name == "BYTES":
        field_dict["kafka_type"] = "BYTES"
        field_dict["type"] = "string"
        field_dict["contentEncoding"] = "base64"
    elif name == "NULLABLE_BYTES":
        field_dict["kafka_type"] = "NULLABLE_BYTES"
        field_dict["oneOf"] = [
            {"type": "string", "contentEncoding": "base64"},
            {"type": "null"}
        ]
    elif name == "RECORDS":
        field_dict["kafka_type"] = "RECORDS"
        field_dict["oneOf"] = [
            {"type": "string", "contentEncoding": "base64"},
            {"type": "null"}
        ]


if __name__ == '__main__':
    main()

