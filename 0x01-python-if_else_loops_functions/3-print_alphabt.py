#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if ['q', 'e'].count(chr(a)) != 0:
        continue
    print("{0}".format(chr(a)), end="")
