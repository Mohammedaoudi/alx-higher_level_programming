#!/usr/bin/python3
"""defines a class_checking function"""


def is_kind_of_class(obj, a_class):
    """chack if an oject is an instance or inherited instance of a_class

    Args:
        obj (any): the object
        a_class (type): the class

    Returns:
        True or False
    """

    if isinstance(obj, a_class):
        return (True)
    return (False)
