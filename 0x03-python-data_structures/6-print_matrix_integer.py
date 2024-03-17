#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for i in range(len(num)):
            if num[i] == num[-1]:
                print("{}".format(num[i]), end="")
            else:
                print("{} ".format(num[i]), end="")
        print()
