#!/usr/bin/python3
"""Working With JSON in Python"""
import json


def load_from_json_file(filename):
    """Reading and Deserialization"""

    with open(filename, 'r', encoding='utf-8') as f:

        return json.load(f)
