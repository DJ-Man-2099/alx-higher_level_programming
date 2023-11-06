#!/usr/bin/python3
"""
9st Module
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object
    if it’s possible
    """
    if not hasattr(obj, '__dict__') and not getattr(obj, '__slots__', None):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)
