#!/usr/bin/python3
"""
Module to deserialize objects to json
"""

import json


def from_json_string(my_str):
    """
    function to deserialize my_obj to json representation
    """

    return json.dumps(my_str)
