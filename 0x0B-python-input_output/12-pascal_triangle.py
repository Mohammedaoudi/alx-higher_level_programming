#!/usr/bin/python3
"""Triangle of Passcal"""


def pascal_triangle(n):
    """my pascal triangle"""
    if n <= 0:
        return ([])

    my_triangle = [[1]]
    while len(my_triangle) != n:
        temp = [1]
        line = my_triangle[-1]
        for i in range(len(line) - 1):
            temp.append(line[i] + line[i + 1])
        temp.append(1)
        my_triangle.append(temp)
    return (my_triangle)
