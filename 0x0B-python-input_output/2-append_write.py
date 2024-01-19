#!/usr/bin/python3
"""ad a text to file"""


def append_write(filename="", text=""):
    """add a text to filename"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
