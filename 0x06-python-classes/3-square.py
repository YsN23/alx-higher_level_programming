#!/usr/bin/python3
"""Square Class Implementation to represent a square"""


class Square:
    """Constructor method to initialize a Square object."""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
