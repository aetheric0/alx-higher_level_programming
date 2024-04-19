#!/usr/bin/python3
"""
Module that extends list class
"""


class MyList(list):
    """
    New Class that extends list class
    """

    def print_sorted(self):
        """
        Sorts the list
        """
        print(sorted(self))
