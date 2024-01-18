#!/usr/bin/python3
"""function inheritance"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (anything): the object
        a_class (type): the class

    Rturns:
        True or False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
