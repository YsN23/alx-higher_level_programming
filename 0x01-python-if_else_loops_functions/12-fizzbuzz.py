#!/usr/bin/python3

"""def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i == 100:
            print("")
        else:
            print("{}".format(i), end=" ")"""

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(f"FizzBuzz", end=" ")
        elif i % 3 == 0:
            print(f"Fizz", end=" ")
        elif i % 5 == 0:
            print(f"Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
