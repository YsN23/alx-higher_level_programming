#!/usr/bin/python3
"""Writing Mode"""


def write_file(filename="", text=""):
    """Function That Writes text into a file and Returns the lenght of the chars"""

    with open(filename, 'w', encoding='utf-8') as f:

        return f.write(text)
