#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments_count = len(sys.argv) - 1

    if not arguments_count:
        print("0 arguments.")
    elif arguments_count == 1:
        print("{} argument:".format(arguments_count))
        print("{}: {}".format(arguments_count, sys.argv[1]))
    else:
        print("{} arguments:".format(arguments_count))
        for index, argument in enumerate(sys.argv[1:]):
            print("{}: {}".format(index + 1, argument))
