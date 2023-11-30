#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    length = len(argv) - 1
    result = 0

    if length == 0:
        print("0")

    else:
        for i in argv[1:]:
            if not isinstance(i, int):
                continue

            result += int(i)
        print("{}".format(result))
