#!/usr/bin/python3
"""
Module to determine if an instance belongs to a class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an exact type of a_class
    """
    return isinstance(obj, a_class)
