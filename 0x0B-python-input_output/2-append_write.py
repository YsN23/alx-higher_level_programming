#!/usr/bin/python3
"""Appending Mode"""


def append_write(filename="", text=""):
    """Append To The EOF and return chars (text)"""

    with open(filename, 'a', encoding="utf-8") as f:

        f.write(text)

        return len(text)
