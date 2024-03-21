#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in matrix:
        for i in num:
            i = i * i
            new_matrix.append(i)
    return new_matrix
