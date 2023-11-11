#!/usr/bin/python3
"""
Class Rectangle inherits from Base.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializer
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        creates the string rep
        of a Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        size setter
        """
        self.width = size
        self.height = size
