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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of the dictionary passed
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Loads JSON string representation
        """
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as file1:
            if list_objs is None:
                file1.write('[]')
                return
            else:
                objs = [obj.to_dictionary() for obj in list_objs]
                file1.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        r1 = cls(4, 3)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name) + '.json'
        try:
            with open(filename, mode='r', encoding='utf-8') as file2:
                data = json.load(file2)
                instances = [cls.create(**item) for item in data]
                return instances
        except FileNotFoundError:
            return []
