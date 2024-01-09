#!/usr/bin/python3
"""Function That Reads a File (UTF-8)"""


def read_file(filename=""):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read()

        print(content)
