#!/usr/bin/python3
"""if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        abj (anything): the object
        a_class (type): the class

    Returns:
        True if the obj is an instance of a_class otherwise False
    """
    if type(obj) == a_class:
        return (True)
    return (False)
