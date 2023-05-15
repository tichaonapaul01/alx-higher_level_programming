#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if len(my_list) == 0:
        pass

    else:
        for element in reversed(my_list):
            print("{:d}".format(element))
