#!/usr/bin/python3
roman_numerical = {
    "IV": 4,
    "IX": 9,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(roman_string):
    sum = 0
    if roman_string is not None and isinstance(roman_string, str):
        for key in ["IV", "IX", "I", "V", "X",
                    "L", "C", "D", "M"]:
            sum += roman_string.count(key)*roman_numerical[key]
            roman_string = roman_string.replace(key, " ")
    return sum
