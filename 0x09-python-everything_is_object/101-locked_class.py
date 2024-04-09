#!/usr/bin/python3
"""
The module 101-locked_class
"""


class LockedClass:
    """
    A class with restricted attribute creation
    """

    __slots__ = ("first_name",)

    def __init__(self):
        self.first_name = None
