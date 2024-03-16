#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if my_list == []:
        return None
    for i in range(len(my_list) - 1):
        if a > my_list[i]:
            continue
        else:
            a = my_list[i]
    return a
