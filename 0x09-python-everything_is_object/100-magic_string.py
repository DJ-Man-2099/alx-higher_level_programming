#!/usr/bin/python3
def magic_string():
    magic_string.invocations += 1
    string = list("BestSchool" for i in range(magic_string.invocations))
    return ", ".join(string)


magic_string.invocations = 0
