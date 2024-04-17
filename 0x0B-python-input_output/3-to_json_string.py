#!/usr/bin/python3
"""
Module to serialize objects to json
"""

import json


def to_json_string(my_obj):
    """
    function to serialize my_obj to json representation
    """

    return json.dumps(my_obj)
