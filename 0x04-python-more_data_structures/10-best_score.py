#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    if a_dictionary is not None:
        max_value = max(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary[key] == max_value:
                max_key = key
                break
    return (max_key)
