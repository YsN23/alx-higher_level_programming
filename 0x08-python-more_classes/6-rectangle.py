#!/usr/bin/python3
"""Rectangle Class Implementation"""


class Rectangle:
    """Real Implementation of Rectangle Class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor"""
        Rectangle.number_of_instances += 1
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

    def __del__(self):
        """Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
