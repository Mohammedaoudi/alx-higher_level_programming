#!/usr/bin/python3
"""Rectangle class define"""


class Rectangle:
    """Rectangle Class

    Args:
        width (int): the width of the rectangle
        height (int):the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        my_list = []
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                my_list.append("#" * self.__width)
        return ('\n'.join(my_list))
