#!/usr/bin/python3
"""
7st Module
"""


class BaseGeometry:
    """
    Empty Class
    """

    def area(self):
        """
        Calculates Area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value is int
        and greater than zero
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    """

    _width = 0
    _height = 0

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
