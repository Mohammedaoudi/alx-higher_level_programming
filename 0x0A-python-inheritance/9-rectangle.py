#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """Initialization a new Rec

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rec"""
        return (self.__width * self.__height)

    def __str__(self):
        """return the string representation"""
        my_str = "[" + str(self.__class__.__name__) + "] "
        my_str += str(self.__width) + "/" + str(self.__height)
        return (my_str)
