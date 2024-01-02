#!/usr/bin/python3
"""Square Class Implementation to represent a square"""


class Square:
    """Constructor method to initialize a Square object."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing Method"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Position Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Printing The Square like that "#" according to area"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                line = " " * self.__position[0] + "#" * self.__size
                if self.__position[1] > 0:
                    line = line[:self.__position[1]] + line[self.__position[1]:]
            print(line)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
