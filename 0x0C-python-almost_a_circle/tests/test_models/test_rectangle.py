#!/usr/bin/python3
"""
Test file for rectangle module
"""

import sys
import unittest
from io import StringIO
from models import rectangle

Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the rectangle module
    """

    def test_width_and_height_only(self):
        rectangle_1 = Rectangle(10, 2)
        self.assertEqual(rectangle_1.id, 1)
        rectangle_2 = Rectangle(2, 10)
        self.assertEqual(rectangle_2.id, 2)

    def test_all_values(self):
        """
        Test for when all arguments are given
        """

        rectangle_3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangle_3.id, 12)

    def test_width_as_string(self):
        """
        Test when a datatype asides int is passed
        """
        self.assertRaises(TypeError, Rectangle, '1', 2)

    def test_no_values(self):
        """
        Test for when Rectangle object receives no argument
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_setters(self):
        """
        Checks if setter functions for arguments work
        """
        rectangle_3 = Rectangle(5, 3)
        rectangle_3.width = 8
        self.assertEqual(rectangle_3.width, 8)

    def test_negative_width(self):
        """
        Tests when negative/0 value is passed to width or height
        """
        with self.assertRaises(ValueError):
            Rectangle(-2, 3)
        with self.assertRaises(ValueError):
            Rectangle(3, -2)
        with self.assertRaises(ValueError):
            Rectangle(3, 2, -4, 6)
        with self.assertRaises(ValueError):
            Rectangle(3, 2, 6, -4)

    def test_area(self):
        """
        Tests the area function that calculates the area using the width
        and height private instance variables
        """

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0,  12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """
        Tests the display function
        """

        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(4, 6)
        r1.display()
        printed_value = captured_output.getvalue().strip()
        self.assertEqual(printed_value, '####\n####\n####\n####\n####\n####')
        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 2)
        r1.display()
        printed_value = captured_output.getvalue().strip()
        self.assertEqual(printed_value, '##\n##')
