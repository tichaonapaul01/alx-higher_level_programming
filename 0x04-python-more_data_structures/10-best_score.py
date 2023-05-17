#!/usr/bin/python3
def best_score(dictionary):
    if not dictionary:
        return None

    max_key = None
    max_value = float('-inf')

    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value

    return max_key
