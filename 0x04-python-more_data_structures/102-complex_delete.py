#!/usr/bin/python3
def delete(dictionary, value):
    keys_to_delete = []
    for key, val in dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del dictionary[key]
