#!/usr/bin/python3
"""
The module print_square prints a square based on the size given
"""


def print_square(size):
    """
    
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    length = 0
    while length < size:
        breadth = 0
        while breadth < size:
            print("#", end="")
            breadth += 1
        length += 1
        print()
