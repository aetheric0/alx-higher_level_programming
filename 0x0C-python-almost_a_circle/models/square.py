#!/usr/bin/python3
"""
The Square Module
"""


from .rectangle import Rectangle

class Square(Rectangle):
    """
    Inherits from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}]'.format(self.id, self.x,
                                                  self.y, self.width)
