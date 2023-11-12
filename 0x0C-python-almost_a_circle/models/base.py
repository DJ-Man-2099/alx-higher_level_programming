#!/usr/bin/python3
"""
the “base” of all other classes in this project.
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        list_to_json = list_dictionaries or []
        return json.dumps(list_to_json)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        list_to_json = list(
            map(lambda obj: obj.to_dictionary(), list_objs)) or []
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as file:
            file.write(Base.to_json_string(list_to_json))
