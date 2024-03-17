#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    a = my_list[0]
    for i in range(len(my_list)):
        if a > my_list[i]:
            continue
        else:
            a = my_list[i]
    return a
