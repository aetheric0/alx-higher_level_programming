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
        """
        Class that validates and assigns width
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
