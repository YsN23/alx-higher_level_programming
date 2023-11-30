#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    fu1 = add(a, b)
    fu2 = sub(a, b)
    fu3 = mul(a, b)
    fu4 = div(a, b)

    print("{} + {} = {}".format(a, b, fu1))
    print("{} - {} = {}".format(a, b, fu2))
    print("{} * {} = {}".format(a, b, fu3))
    print("{} / {} = {}".format(a, b, fu4))
