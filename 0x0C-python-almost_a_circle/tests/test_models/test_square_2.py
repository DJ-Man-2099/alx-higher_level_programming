#!/usr/bin/python3
"""Unittest for Square Class
"""
import unittest
from models.square import Square, __doc__
from models.base import Base, __doc__
from tests.helpers import Helpers


class TestSquareClass(unittest.TestCase):
    """
    Class for Unit Testing Square

    this class checks for every detail in the class
    """

    def setUp(self):
        # Reset the class ids before each test
        Base.reset_before_tests()

    def test_size_doc(self):
        """
        Testing docs exist
        """
        self.assertIsNotNone(Square.size.__doc__)
        self.assertNotEqual(Square.size.__doc__, "")

    def test_size(self):
        """
        Testing size with validation
        """
        helper = Helpers()

        s1 = Square(5)
        helper.stdout(lambda: print(s1), "[Square] (1) 0/0 - 5\n")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        helper.stdout(lambda: print(s1), "[Square] (1) 0/0 - 10\n")

        with self.assertRaises(TypeError) as terror:
            s1.size = "9"
        self.assertEqual(str(terror.exception), "width must be an integer")


if __name__ == '__main__':
    unittest.main()
