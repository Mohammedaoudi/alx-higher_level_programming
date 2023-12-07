#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    nouv = set_1.difference(set_2)
    nouv = nouv.union(set_2.difference(set_1))
    return (nouv)
