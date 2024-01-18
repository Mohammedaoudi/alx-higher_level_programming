#!/usr/bin/python3
"""function adds an attribute"""


def add_attribute(obje, attri, val):
    """Adds a new attribute to an object

    Args:
        obje (anything): the object
        attri (str): the name of the attribute
        val (anything): the value of attri

    Raises:
        TypeError: if the att cannot be added
    """

    if not hasattr(obje, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obje, attri, val)
