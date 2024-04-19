#!/usr/bin/python3
"""
An empty class module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Inherits BaseGeometry from module 7-base_geometry

    __init__(self, width, height):
    =============================
    Initializes private instance variables width and height for the class
    """
    def __init__(self, width, height):
        self.__width = BaseGeometry.integer_validator(self, None, width)
        self.__height = BaseGeometry.integer_validator(self, None, height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] 3/5'
