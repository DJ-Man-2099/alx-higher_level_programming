#!/usr/bin/python3
"""
Module for fourth task
Using Tests to check task if successful

"""


def print_square(size) -> None:
    """
    This Function prints a square with the character #

    params: size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")
