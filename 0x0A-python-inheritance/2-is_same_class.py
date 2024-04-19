#!/usr/bin/python3
"""
Module to determine if an instance belongs to a class
"""


def is_same_class(obj, a_class):
    """
    checks if obj is an exact type of a_class
    """
    return type(obj) is a_class
