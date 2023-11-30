#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    lenght = len(argv) - 1
    result = 0

    if lenght == 0:
        print("0")

    else:
        for i in argv[1:]:
            if not i.isdigit():
                continue

            result += int(i)
        print("{}".format(result))
