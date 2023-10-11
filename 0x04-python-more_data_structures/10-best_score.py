#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    if a_dictionary is not None:
        score_list = list(
            filter(lambda value: value is not None, a_dictionary.values()))
        if len(score_list) != 0:
            max_value = max(score_list)
            for key in a_dictionary.keys():
                if a_dictionary[key] == max_value:
                    max_key = key
                    break
    return (max_key)
