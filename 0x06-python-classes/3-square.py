#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): private instance size of the square
    """
    def __init__(self, size=0):
        """initiation of the class
        Args:
            size (int): The size of the square.
        """
        if type(size) is int:
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Area of the square"""
        return (self.__size ** 2)
