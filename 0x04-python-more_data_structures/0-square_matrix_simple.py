#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    row = []
    for num in matrix:
        for i in num:
            i = i * i
            row.append(i)
        new_matrix.append(row)
        row = []
    return new_matrix
