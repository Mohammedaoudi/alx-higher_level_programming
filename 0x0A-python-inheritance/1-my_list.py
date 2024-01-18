#!/usr/bin/python3
"""creating Mylist"""


class MyList(list):
    """Mylist class inherits from a list"""

    def print_sorted(self):
        my_list = sorted(self)
        print(my_list)
