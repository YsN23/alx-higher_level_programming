#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if not argv or len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))

    else:
        print("{} arguments:".format(len(argv) - 1))
        for i, args in enumerate(argv[1:]):

            print("{}: {}".format(i + 1, args))
