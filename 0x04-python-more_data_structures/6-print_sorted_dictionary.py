#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keis = sorted(a_dictionary.keys())
    for i in keis:
        print("{}: {}".format(i, a_dictionary.get(i)))
