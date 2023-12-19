#!/usr/bin/python3
"""Square Class Implementation to represent a square"""


class Square:
    """Constructor method to initialize a Square object."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Property for Size Setting"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")


    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
