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
        self.__size = size

    @property
    def size(self):
        """Retreive size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) is int:
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #:"""
        x = self.__size
        if x == 0:
            print()
        else:
            for i in range(x):
                for j in range(x):
                    print("#", end="")
                print()
