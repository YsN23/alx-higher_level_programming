#!/usr/bin/python3
"""Rectangle Class Implementation"""


class Rectangle:
    """Real Implementation of Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares Two Instances according to area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_rect_1 = rect_1.area()
        area_rect_2 = rect_2.area()

        if area_rect_1 == area_rect_2 or area_rect_1 > area_rect_2:
            return rect_1

        else:
            return rect_2

    def __str__(self):
        square = ""
        if self.__width == 0 or self.__height == 0:
            return square
        for i in range(self.__height):
            for j in range(self.__width):
                square += str(self.print_symbol)
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
