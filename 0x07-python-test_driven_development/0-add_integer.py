#!/usr/bin/python3
"""A function that adds two integres
    Args:
        a (int/float): the first element
        b (int/float): the second element initilized by 98
"""


def add_integer(a, b=98):
    """Return the integer addidtion of a and b

    float args are casted into int

    Raises:
        TypeError: if a or b are not int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
