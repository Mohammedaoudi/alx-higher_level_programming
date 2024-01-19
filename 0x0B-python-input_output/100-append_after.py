#!/usr/bin/python3
"""insert after a string"""


def append_after(filename="", search_string="", new_string=""):
    """adds a string in a specified position"""
    new_txt = ""
    with open(filename) as f:
        for i in f:
            new_txt += i
            if search_string in i:
                new_txt += new_string
    with open(filename, "w") as a:
        a.write(new_txt)
