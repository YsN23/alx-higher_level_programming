#!/usr/bin/python3
"""Working With JSON in Python"""
import json


def from_json_string(my_str):
    """Deserialization """

    py_obj = json.loads(my_str)

    return py_obj
