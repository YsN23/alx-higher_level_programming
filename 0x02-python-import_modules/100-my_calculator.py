#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == "+":
            re1 = add(a, b)
            print("{} + {} = {}".format(a, b, re1))

        elif op == "-":
            re2 = sub(a, b)
            print("{} - {} = {}".format(a, b, re2))

        elif op == "*":
            re3 = mul(a, b)
            print("{} * {} = {}".format(a, b, re3))

        elif op == "/":
            re4 = div(a, b)
            print("{} / {} = {}".format(a, b, re4))

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
