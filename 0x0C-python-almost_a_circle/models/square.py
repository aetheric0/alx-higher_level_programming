#!/usr/bin/python3
"""
The Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}]'.format(self.id, self.x,
                                                  self.y, self.width)

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

    def to_dictionary(self):
        """
        Prints dictionary representation of object
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value > 0:
                self.width = value
                self.height = value
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')
