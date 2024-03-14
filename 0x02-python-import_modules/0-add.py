#!/usr/bin/python3

# Import function add(a, b) from module add_0 and prints
# addition of arguments passed to imported function
# Would not execute if __import__ is used

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
