#!/usr/bin/python3
"""Working With JSON in Python"""
import json


def save_to_json_file(my_obj, filename):
    """Serialization and Writing To JSON file"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
