#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nouv = dict()
    for i in list(a_dictionary.keys()):
        nouv[i] = a_dictionary[i] * 2
    return (nouv)
