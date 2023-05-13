#!/usr/bin/python3
import sys

def add_args(*args):
    result = 0
    for arg in args:
        result += int(arg)
    print(result)

if __name__ == "__main__":
    add_args(*sys.argv[1:])
