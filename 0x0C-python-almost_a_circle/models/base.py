#!/usr/bin/python3
"""
the “base” of all other classes in this project.
"""


class Base:
    """
    The Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing
        """
        new_id = id
        if new_id is None:
            Base.__nb_objects += 1
            new_id = Base.__nb_objects
        self.id = new_id

    @staticmethod
    def reset_before_tests():
        """
        Resets The __nb_objects
        FOR TESTING ONLY
        """
        Base.__nb_objects = 0
