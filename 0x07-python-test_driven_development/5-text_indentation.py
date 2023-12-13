#!/usr/bin/python3
"""
Module for fifth task
Using Tests to check task if successful

"""


def text_indentation(text) -> None:
    """
    This Function prints a text with 2 new lines
    after each of these characters: ., ? and :

    params: text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for index in range(len(text)):
        if text[index] in ["?", ":", "."]:
            text = "\n\n".join([text[:index+1], text[index+1:]])
        index += 2
    string_array = text.splitlines()
    for index in range(len(string_array)-1):
        print(string_array[index].strip())
    print(string_array[-1].strip(), end="")
