#!/usr/bin/python3
"""define a square class"""


class Square:
    """define a square
    Attributes:
     __size(int): size of the square privat"""

    def __init__(self, size=0):
        """the initiation of the class
        Args:
        __size(int):the size of square"""
        if type(size) is int:
            if (size >= 0):
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """square s area"""
        return(self.__size ** 2)
