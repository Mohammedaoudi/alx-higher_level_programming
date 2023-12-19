#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): private instance size of the square
        __position(tuple(2)):position private instance
    """
    def __init__(self, size=0, position=(0, 0)):
        """initiation of the class
        Args:
            __position(tuple(2)): position
            __size (int): The size of the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """set position"""
        if (isinstance(value, tuple) and len(value) == 2 and
        all(el >= 0 for el in value) and
        all(isinstance(el, int) for el in value)):
            self.__position == value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints in stdout the square with the character #:"""
        x = self.__size
        y = self.__position
        if x == 0:
            print()
        else:
            for i in range(y[1]):
                print()
            for j in range(x):
                for i in range(y[0]):
                    print(" ", end="")
                for i in range(x):
                    print("#", end="")
                print()
