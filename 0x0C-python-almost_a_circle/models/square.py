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
        """
        Initializes the object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Sets the str method when str() is called
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the values using args and kwargs
        """
        if args:
            i = 0
            self.id = args[i]
            i += 1
            if i < len(args):
                self.size = args[i]
            i += 1
            if i < len(args):
                self.x = args[i]
            i += 1
            if i < len(args):
                self.y = args[i]
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
        """
        getter property for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the value for size
        """
        if type(value) is int:
            if value > 0:
                self.width = value
                self.height = value
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')
