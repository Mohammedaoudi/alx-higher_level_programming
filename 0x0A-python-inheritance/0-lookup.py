#!/usr/bin/python3
"""lookup for methods and attrivute of a class"""


def lookup(obj):
    """returns a list of attributes and methods of a class

    Args:
        obj (object): the object to be used
    Returns:
        list of attributs
    """
    my_list = []
    for item in dir(obj):
        my_list.append(item)

    return (my_list)
