#!/usr/bin/python3
"""function that divides all elements of a matrix.

    Args:
        matrix (list): the matrix
        div (int/float): the div
"""


def matrix_divided(matrix, div):
    """return a new matrix with all elements devided by div

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
"""
    if (
            type(matrix) is not list or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(ele, int) or isinstance(ele, float)
                for ele in [num for row in matrix for num in row]
            )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of "
            "integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
