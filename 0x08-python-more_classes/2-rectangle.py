#!/usr/bin/python3
"""Rectangle Class Implementation"""


class Rectangle:
    """Real Implementation of Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Constructor"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Area of The Rectangle"""
        area = self.__height * self.__width
        return area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = (self.__height + self.__width) * 2

        return perimeter
