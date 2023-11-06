#!/usr/bin/python3
"""
9st Module
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object
    if it’s possible
    """
    if obj is None or (not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__')):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
