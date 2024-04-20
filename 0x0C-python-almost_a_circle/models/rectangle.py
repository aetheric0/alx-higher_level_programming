#!/usr/bin/python3
"""
Module that inherits from Base
"""


from .base import Base

class Rectangle(Base):
    """
    Initializes the private instance attributes and sets their
    getters and setters methods
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def width(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def width(self, value):
        self.__x = value


    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.__y = value
