#!/usr/bin/python3
"""
Module to load object from json
"""
import json


def load_from_json_file(filename):
    """
    Function that loads the json
    """

    with open(filename, encoding="utf-8") as file:
        a = json.loads(file.read())
    return a
