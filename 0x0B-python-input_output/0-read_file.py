#!/usr/bin/python3
"""
Documentation for 0-read_file module
Contains read_file function that reads a file to stdout
"""


def read_file(filename=""):
    """
    Function that reads a file
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
