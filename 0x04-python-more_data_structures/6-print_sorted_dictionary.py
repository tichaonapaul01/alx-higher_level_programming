#!/usr/bin/python3
def print_sorted_dictionary(dictionary):
    sorted_keys = sorted(dictionary.keys())
    for key in sorted_keys:
        value = dictionary[key]
        print(f"{key}: {value}")
