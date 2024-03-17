#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for i in range(len(num)):
            if num[i] == num[-1]:
                print("{:d}".format(num[i]), end="")
            else:
                print("{:d} ".format(num[i]), end="")
        print()
