#!/usr/bin/python3
def uppercase(str):
    upper_string = ""

    for char in str:
        ascii_num = ord(char)

        if 97 <= ascii_num <= 122:
            new_ascii = ascii_num - 32
            upper_char = chr(new_ascii)
            upper_string += upper_char

        else:
            upper_string += char

    print("{}".format(upper_string))
