#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif num_args == 1:
        print("Number of argument(s): 1. Argument:")
        print("1: " + sys.argv[1])
    else:
        print("Number of argument(s): " + str(num_args) + ". Arguments:")
        for i in range(1, num_args + 1):
            print(str(i) + ": " + sys.argv[i])
