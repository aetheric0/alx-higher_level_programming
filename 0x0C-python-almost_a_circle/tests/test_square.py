#!/usr/bin/python3
"""
Test module for square module
"""
import sys
import unittest
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the square module
    """

    def test_initialization(self):
        """
        Tests square output using '#'
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Square(5)
        r1.display()
        printed_value = captured_output.getvalue().strip()
        self.assertEqual(printed_value, '#####\n#####\n#####\n#####\n#####')
