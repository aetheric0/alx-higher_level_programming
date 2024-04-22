#!/usr/bin/python3
"""
unit test module for `base` module in models directory
"""


import unittest
from models import base

Base = base.Base


class TestBase(unittest.TestCase):
    """
    Test cases for `base` class
    """

    def test_integer(self):
        """
        Testing when an integer is passed
        """
        result = Base(2)
        self.assertEqual(result.id, 2)

    def test_none(self):
        """
        Testing increment when `None` passed as value
        """
        result = Base(None)
        self.assertEqual(result.id, 1)
        result = Base(None)
        self.assertEqual(result.id, 2)

if __name__ == '__main__':
    unittest.main()
