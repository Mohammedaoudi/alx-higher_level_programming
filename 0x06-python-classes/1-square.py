#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """defines a square
       Attributes:
        __size (int): private instance size of the square"""

    def __init__(self, size):
        """initiation of the class
        Args:
            size (int): The size of the square.
        """
        self.__size = size
