#!/usr/bin/python
"""Unittest for Rectangle Class
"""
from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle, __doc__
from models.base import Base, __doc__


class TestRectangleClass(unittest.TestCase):
    """
    Class for Unit Testing Rectangle

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_display_str_doc(self):
        """
        Testing display()
        and __str__() docs exist
        """
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertNotEqual(Rectangle.display.__doc__, "")
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertNotEqual(Rectangle.__str__.__doc__, "")

    def test_display(self):
        """
        Testing display
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(4, 6)
        r1.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, """####
####
####
####
####
####
""")
        print("---")

        captured_output = StringIO()
        sys.stdout = captured_output
        r1 = Rectangle(2, 2)
        r1.display()
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, """##
##
""")

    def test_str(self):
        """
        Testing __str__
        """

        r1 = Rectangle(4, 6)
        self.assertEqual(str(r1), """####
####
####
####
####
####""")

        r1 = Rectangle(2, 2)
        self.assertEqual(str(r1), """##
##""")


if __name__ == '__main__':
    unittest.main()
