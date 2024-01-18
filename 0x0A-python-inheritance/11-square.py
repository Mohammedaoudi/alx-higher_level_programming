#!/usr/bin/python3
"""Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initialization

        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """print formated"""
        my_str = "[" + str(self.__class__.__name__) + "] "
        my_str += str(self.__size) + "/" + str(self.__size)
        return (my_str)
