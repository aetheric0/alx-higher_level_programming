#!/usr/bin/python3
"""
The module 1-Rectangle which returns/sets the width and height
"""


class Rectangle:
    """
    The Rectangle class
    ====================

    Defines class getter and setter attributes that retrieves or sets
    the width and height of the class
    """

    def __init__(self, width=0, height=0):
        """
        Initializing the class rectangle

        Args:
        -----
        width: the width of the rectangle
        height: the height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Retrieving/Modifying the private instance variable width"""

        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    """ Retrieving/Modifying the private instance variable height"""

    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
