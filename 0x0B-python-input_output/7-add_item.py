#!/usr/bin/python3
"""
8th Task
"""


import sys


if __name__ == "__main__":
    """
    adds all arguments to a Python list,
    and then save them to a file
    """
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    old_list = load_from_json_file("add_item.json")
    if old_list is None:
        old_list = []
    old_list.extend(sys.argv)
    save_to_json_file("add_item.json", old_list)
