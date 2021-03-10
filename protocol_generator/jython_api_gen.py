# Note: This file is meant to be run with Jython2.7
# Use generate_api_definition.py to do that for you

# Unless we want to add shims for all Java classes that are used here, we won't be able to type check this file
# type: ignore

import json
import os
from collections import OrderedDict

from org.apache.kafka.common.acl import AclOperation, AclPermissionType
from org.apache.kafka.common.errors import RetriableException
from org.apache.kafka.common.protocol import ApiKeys, Errors
from org.apache.kafka.common.protocol.types import ArrayOf, Schema, Type
from org.apache.kafka.common.resource import PatternType, ResourceType

FIELD_NAME_TO_ENUM_CLASS = {
    "api_key": "ApiKey",
    "error_code": "ErrorCode",
    "resource_type": "ResourceType",
    "resource_pattten_type": "ResourcePatternType",
    "resource_pattten_type_filter": "ResourcePatternType",
    "operation": "AclOperation",
    "permission_type": "AclPermissionType",
}


def main():
    dump_api_definitions()
    dump_constants()


def dump_api_definitions():
    api_definition = [api_key_to_dict(api_key) for api_key in ApiKeys.values()]
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, "api_definition.json")
    with open(path, "w") as o:
        json.dump(api_definition, o, indent=2)


def api_key_to_dict(api_key):
    api_dict = OrderedDict()
    api_dict["api_key"] = api_key.id
    api_dict["api_name"] = str(api_key)
    api_dict["cluster_action"] = api_key.clusterAction
    api_dict["request_schemas"] = [create_type_data(schema) for schema in api_key.requestSchemas]
    api_dict["response_schemas"] = [create_type_data(schema) for schema in api_key.responseSchemas]
    return api_dict


def resolve_field(field):
    field_dict = create_type_data(field.type)
    field_dict["name"] = field.name
    field_dict["doc"] = field.docString
    field_dict["default"] = field.defaultValue
    field_dict["has_default"] = field.hasDefaultValue

    if field.name in FIELD_NAME_TO_ENUM_CLASS:
        make_enum_field(field_dict)
    return field_dict


def create_type_data(type_):
    field_dict = OrderedDict()
    if isinstance(type_, Schema):
        field_dict["type"] = "STRUCT"
        schema_fields = []
        for field in type_.fields():
            schema_fields.append(resolve_field(getattr(field, "def")))
        field_dict["fields"] = schema_fields
    elif isinstance(type_, ArrayOf):
        field_dict["type"] = "ARRAY"
        type_dict = create_type_data(type_.type())
        field_dict["element_type"] = type_dict
    elif isinstance(type_, Type.DocumentedType):
        field_dict["type"] = type_.typeName()
    else:
        raise ValueError("Unkown type %s" % type_)
    return field_dict


def make_enum_field(field_dict):
    assert field_dict["name"] in FIELD_NAME_TO_ENUM_CLASS
    field_dict["primitive_type"] = field_dict["type"]
    field_dict["type"] = "ENUM"
    field_dict["enum_class"] = FIELD_NAME_TO_ENUM_CLASS[field_dict["name"]]


def dump_constants():
    constants = collect_constants()
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, "constant_definition.json")
    with open(path, "w") as o:
        json.dump(constants, o, indent=2)


def collect_constants():
    constants = {
        "ApiKey": get_api_key_constants(),
        "ErrorCode": get_error_code_constants(),
        "ResourceType": get_resource_type_constants(),
        "ResourcePatternType": get_resource_pattern_type_constants(),
        "AclOperation": get_acl_operation_constants(),
        "AclPermissionType": get_acl_permission_type_constants(),
    }
    return constants


def get_api_key_constants():
    return {
        "enum": [{"name": str(api_key), "value": api_key.id} for api_key in ApiKeys.values()],
        "primitive_type": "INT16",
    }


def get_error_code_constants():
    data = {"enum": [], "meta": [], "primitive_type": "INT16"}
    for err in Errors.values():
        data["enum"].append({"name": str(err), "value": err.code()})
        meta = OrderedDict([("value", err.code()), ("retryable", False), ("default_message", "")])
        exc = err.exception()
        if exc is not None:
            meta["retryable"] = isinstance(exc, RetriableException)
            meta["default_message"] = exc.getMessage()
        data["meta"].append(meta)
    return data


def get_resource_type_constants():
    return get_enum_name_and_code(ResourceType, "INT8")


def get_enum_name_and_code(enum, primitive_type):
    return {
        "primitive_type": primitive_type,
        "enum": [{"name": str(elem), "value": elem.code()} for elem in enum.values()],
    }


def get_resource_pattern_type_constants():
    return get_enum_name_and_code(PatternType, "INT8")


def get_acl_operation_constants():
    return get_enum_name_and_code(AclOperation, "INT8")


def get_acl_permission_type_constants():
    return get_enum_name_and_code(AclPermissionType, "INT8")


if __name__ == "__main__":
    main()
