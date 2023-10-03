#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print('{}'.format(chr(ord(c)+ord('A')-ord('a'))), end="")
        else:
            print('{}'.format(c), end="")
    print("")
