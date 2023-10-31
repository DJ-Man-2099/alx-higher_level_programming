#!/usr/bin/python3
"""
Module for third task
Using Tests to check task if successful

"""


def say_my_name(first_name, last_name="") -> None:
    """
    This Function prints "My name is <first name> <last name>"

    params: first_name
            last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
