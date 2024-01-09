#!/usr/bin/python3
"""Working With JSON in Python"""
import json


def save_to_json_file(my_obj, filename):
    """Serialization and Writing To JSON file"""

    json_format_string = json.dumps(my_obj)

    with open(filename, 'w') as f:
        f.write(json_format_string)
