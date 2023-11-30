#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = sum(int(arg) for arg in sys.argv[1:])
    else:
        result = 0

    print(result)
