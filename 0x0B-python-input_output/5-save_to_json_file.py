#!/usr/bin/python3
"""
module to write python object to json
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function to save python object to json
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
