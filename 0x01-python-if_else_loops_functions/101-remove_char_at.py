#!/usr/bin/python3
def remove_char_at(s, n):
    # Check if the index is valid
    if n < 0 or n >= len(s):
        return s
    # Create a new string with the characters before and after the index
    return s[:n] + s[n+1:]
