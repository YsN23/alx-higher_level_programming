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

    def __str__(self):
        square = ""
        if self.__width == 0 or self.__height == 0:
            return square
        for i in range(self.__height):
            for j in range(self.__width):
                square += "#"
            if i != self.__height - 1:
                square += "\n"
        return square

    def __repr__(self):
        """Repr Method"""
        return f"Rectangle({self.__width}, {self.__height})"


my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

