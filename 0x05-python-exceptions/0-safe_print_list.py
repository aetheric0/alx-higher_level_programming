#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in my_list:
            if i < x:
                print("{}".format(item), end="")
                i += 1
        print()
        return (i)
    except Exception:
        print("Error: Could not access list")
