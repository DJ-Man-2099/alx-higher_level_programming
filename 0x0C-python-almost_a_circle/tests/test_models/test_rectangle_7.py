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

    def test_update_doc(self):
        """
        Testing update() docs exist
        """
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertNotEqual(Rectangle.update.__doc__, "")

    def test_update(self):
        """
        Testing update
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(10, 10, 10, 10)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (1) 10/10 - 10/10\n")
        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(89)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 10/10 - 10/10\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(89, 2)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 10/10 - 2/10\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(89, 2, 3)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 10/10 - 2/3\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(89, 2, 3, 4)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 4/10 - 2/3\n")

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.update(89, 2, 3, 4, 5)
        print(r1)
        printed_output = captured_output.getvalue()
        self.assertEqual(printed_output, "[Rectangle] (89) 4/5 - 2/3\n")


if __name__ == '__main__':
    unittest.main()
