#!/usr/bin/python3
"""
Documentation for 1-write_file module
Contains write_file function that appends text to a file
"""


def write_file(filename="", text=""):
    """
    Function that appends to filename
    Returns the numbers of characters written
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        a = file.write(text)
    return a
