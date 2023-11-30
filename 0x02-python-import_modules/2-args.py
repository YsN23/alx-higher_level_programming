#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if not sys.argv or len(sys.argv) == 1:
        print(f"0 arguments.")

    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i, args in enumerate(sys.argv[1:]):

            print("{}: {}".format(i + 1, args))
