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
        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')

        super().__init__(id)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def area(self):
        """
        Calculates the area from the width and height
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the area using the character '#'
        """
        for length in range(self.__height):
            if self.__y > 0 and length == 0:
                for i in range(self.__y):
                    print()
            for breadth in range(self.__width):
                if self.__x > 0 and breadth == 0:
                    for j in range(self.__x):
                        print(' ', end="")
                print('#', end ="")
            print()

    def update(self, *args, **kwargs):
        if args:
            i = 0
            self.id = args[i]
            i += 1
            if i < len(args):
                self.__width = args[i]
            i += 1
            if i < len(args):
                self.__height = args[i]
            i += 1
            if i < len(args):
                self.__x = args[i]
            i += 1
            if i < len(args):
                self.__y = args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')



    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')
