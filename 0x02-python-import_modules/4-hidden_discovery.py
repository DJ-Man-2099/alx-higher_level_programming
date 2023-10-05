#!/usr/bin/python3

def no_prefix(value):
    return not value.startswith("__")


if __name__ == "__main__":
    names = list(filter(no_prefix, dir('hidden_4.pyc')))
    for name in names:
        print(name)
