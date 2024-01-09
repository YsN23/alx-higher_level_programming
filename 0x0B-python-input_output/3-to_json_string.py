#!/usr/bin/python3
"""Working With JSON in Python"""

import json

def to_json_string(my_obj):
    """Serialization"""

    json_string = json.dumps(my_obj)

    return json_string
