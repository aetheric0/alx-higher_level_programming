#!/usr/bin/python3

"""
The module matrix_divided for dividing a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by div.

    Args:
        matrix (list of lists): The matrix.
        div (int or float): The divisor

    Returns:
        new_matrix: The divided matrix rounded to 2 decimal places

    Raises:
        TypeError: If div or the elements in the matrix are not int or float
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a  number")
    row = 0
    for row in range(len(matrix) - 1):
        if len(matrix[row]) != len(matrix[row+1]):
            raise TypeError("Each row of the matrix nust have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix" +
                                " list of lists) of integers/floats")
            new_item = round(item / div, 2)
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
