#!/usr/bin/python3
"""Function That Reads a File (UTF-8)"""


def read_file(filename=""):
    """Read a File and Print it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:

        content = f.readlines()

        print(content, end="")
