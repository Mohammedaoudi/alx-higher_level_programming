#!/usr/bin/python3
"""function prints a quare"""


def print_square(size):
    """Print a square

    Args:
        size (int): The height and width of square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
