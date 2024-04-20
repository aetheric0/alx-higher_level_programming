#!/usr/bin/python3
"""
Module containing the first class
"""


class Base():
    """
    class with private class attribute and __init__
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class with specific conditions
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
