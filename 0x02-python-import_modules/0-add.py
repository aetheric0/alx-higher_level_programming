#!/usr/bin/python3

# Import function add(a, b) from module add_0 and prints
# addition of arguments passed to imported function
# Would not execute if __import__ is used


a = 1
b = 2

from add_0 import add
print("{} + {} = {}".format(a, b, add(a, b)))
