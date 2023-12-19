#!/usr/bin/python3
"""class defines square"""


class Square:
    """ defines square
    Attributes:
    __size(int): private instance """

    def __init__(self, size=0):
        """the initiation of the class
        Args:
        __size(int):the size of the square"""
        self.__size = size

    @property
    def size(self):
        """retrieve size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """area of the square"""
        return(self.__size ** 2)
