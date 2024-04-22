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
