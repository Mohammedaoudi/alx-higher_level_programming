#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    addit = set()
    for i in my_list:
        addit.add(i)
    for j in addit:
        s += j
    return (s)
