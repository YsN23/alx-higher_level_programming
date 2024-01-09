#!/usr/bin/python3
"""Writing Mode"""


def write_file(filename="", text=""):
    """Function That Writes text into a file and Returns num of chars"""

    with open(filename, 'w', encoding='utf-8') as f:

        f.write(text)

        return len(text)
