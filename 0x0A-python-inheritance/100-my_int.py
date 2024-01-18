#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """Equal == eq || NotEqual == ne

    Args:
        val (int): the value to be chcked
    """
    def __eq__(self, val):
        """Not Equal"""
        return (self.real != val)

    def __ne__(self, val):
        """Equal"""
        return (self.real == val)
