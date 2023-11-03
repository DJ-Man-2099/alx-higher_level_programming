#!/usr/bin/python
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for Unit Testing max_integer

    this class checks for every detail in the function
    """

    def test_max(self):
        """
        checks if it calculated max correctly
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_empty_list(self):
        """
        checks if it handles empty lists correctly
        """
        self.assertEqual(max_integer([]), None)

    def test_one_list(self):
        """
        checks if it handles empty lists correctly
        """
        self.assertEqual(max_integer([1]), 1)

    def test_neg(self):
        """
        checks if it handles one neg correctly
        """
        self.assertEqual(max_integer([-1, 2, 3]), 3)

    def test_neg_list(self):
        """
        checks if it handles neg lists correctly
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)


if __name__ == '__main__':
    unittest.main()
