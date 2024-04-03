#!/usr/bin/python3

""" Creates a class with private instance attribute and validation"""


class Square:
    """ private instance attribute with validation"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
