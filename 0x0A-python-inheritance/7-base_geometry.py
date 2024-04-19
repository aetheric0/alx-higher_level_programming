#!/usr/bin/python3
"""
An empty class module
"""


class BaseGeometry():
    """
    Empty Class
    """
    def area(self):
        """
        Area has not been implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value of 'value' passed
        """
        if isinstance(value, int):
            if value > 0:
                return value
            else:
                raise ValueError("<name> must be greater than 0")
        else:
            raise TypeError("<name> must be an integer")
