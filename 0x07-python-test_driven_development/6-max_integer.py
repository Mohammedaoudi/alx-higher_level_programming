#!/usr/bin/python3
"""find max of list"""


def max_integer(list=[]):
    """function finds the max of a list
    if it's empty, it returns None
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return (result)
