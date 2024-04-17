#!/usr/bin/python3
"""
Documentation for 1-write_file module
Contains write_file function that writes to a file
"""


def write_file(filename="", text=""):
    """
    Function that writes to filename
    Returns the numbers of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        a = file.write(text)
    return a
