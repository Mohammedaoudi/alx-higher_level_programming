#!/usr/bin/python3
"""defines a function that print a name."""


def say_my_name(first_name, last_name=""):
    """print name.

    Args:
        first_name (str): The first name
        last_name (str): The family name
    Raises:
        TypeError: if either first or last name are not str
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
