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
    
    def test_empty_list(self):
        """
        checks if it handles empty lists correctly
        """
        self.assertEqual(max_integer([]),None)

if __name__ == '__main__':
    unittest.main()