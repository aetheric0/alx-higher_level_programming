#!/usr/bin/python3
"""
Module that adds all argumetns to a Python list, and saves
a JSON representation to a file
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_argument():
    """
    Appends arguments from terminal and saves json representation to
    file add_item.json
    """

    filename = 'add_item.json'
    arg_list = []

    with open(filename, encoding='utf-8') as my_file:
        file_content = my_file.read()
        if len(file_content) > 0:
            json_arg = json.loads(file_content)
            arg_list += json_arg

    for arg in sys.argv[1:]:
        arg_list.append(arg)

    save_to_json_file(arg_list, filename)
    json_arg = load_from_json_file(filename)
    return json_arg


add_argument()
