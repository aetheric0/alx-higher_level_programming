#!/usr/bin/python3
"""
Module containing the first class
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of the dictionary passed
        """
        if list_dictionaries is None or list_dictionaries[0] is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
