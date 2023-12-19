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
        if type(value) is int or type(value) is float:
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a number")

    def area(self):
        """Area of the square"""
        return (self.__size ** 2)

    def __lt__(self, other):
        if isinstance(other, Square):
            return (self.area() < other.area())

    def __gt__(self, other):
        if isinstance(other, Square):
            return (self.area() > other.area())

    def __eq__(self, other):
        if isinstance(other, Square):
            return (self.area() == other.area())

    def __ne__(self, other):
        if isinstance(other, Square):
            return (self.area() != other.area())

    def __ge__(self, other):
        if isinstance(other, Square):
            return (self.area() >= other.area())

    def __le__(self, other):
        if isinstance(other, Square):
            return (self.area() <= other.area())

    def __lt__(self, other):
        if isinstance(other, Square):
            return (self.area() < other.area())
