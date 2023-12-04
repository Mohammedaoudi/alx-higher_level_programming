#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    max1 = my_list[0]
    for i in my_list:
        if i > max1:
            max1 = i
    return (max1)
