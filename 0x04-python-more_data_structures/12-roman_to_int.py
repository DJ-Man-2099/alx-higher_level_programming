#!/usr/bin/python3
roman_numerical = {
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
    if roman_string is not None:
        for i in roman_string:
            sum += roman_numerical[i]
    return sum
