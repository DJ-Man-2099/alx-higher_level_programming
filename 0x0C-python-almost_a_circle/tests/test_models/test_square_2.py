#!/usr/bin/python3
"""Unittest for Square Class
"""
import unittest
from models.square import Square, __doc__
from models.base import Base, __doc__
from help_functions.helpers import Helpers


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

        with self.assertRaises(ValueError) as terror:
            s2 = Square(0)
        self.assertEqual(str(terror.exception), "width must be > 0")

    def test_square_size1(self):
        """ test without args """
        with self.assertRaises(TypeError):
            Square.size()

    def test_square_size2(self):
        """test getter"""
        my_square = Square(2)
        self.assertEqual(my_square.size, 2)

    def test_square_size3(self):
        """test setter"""
        my_square = Square(2)
        my_square.size = 7
        self.assertEqual(my_square.size, 7)

    def test_square_size4(self):
        """test setter with 0"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = 0

    def test_square_size5(self):
        """test setter with negative value"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = -5

    def test_square_size6(self):
        """test setter with wrong type: float"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = 4.5

    def test_square_size7(self):
        """test setter with wrong type: string"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = "School"

    def test_square_size8(self):
        """test setter with wrong type: list"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = [4]

    def test_square_size9(self):
        """test setter with wrong type: tuple"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = (4, )

    def test_square_size10(self):
        """test setter with wrong type: dictionary"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = {4}


if __name__ == '__main__':
    unittest.main()
