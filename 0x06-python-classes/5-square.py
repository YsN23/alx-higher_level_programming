#!/usr/bin/python3
"""Square Class Implementation to represent a square"""


class Square:
    """Constructor method to initialize a Square object."""
    def __init__(self, size=0):
        """Initializing Method"""
        self.__size = size


    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property for Size Setting"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Printing Method"""
        if self.__size == 0:
            print()
        else:
            for not_space in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
