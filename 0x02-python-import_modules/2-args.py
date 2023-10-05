#!/usr/bin/python3
import sys


if __name__ == "__main__":
    args = sys.argv
    num_args = len(args)
    str_num = f"{num_args} {'argument' if num_args == 1 else 
                            'arguments'}{':' if num_args > 0 else '.'}"
    print(str_num)
    for arg in range(num_args):
        print(f"{arg+1}: {args[arg]}")
