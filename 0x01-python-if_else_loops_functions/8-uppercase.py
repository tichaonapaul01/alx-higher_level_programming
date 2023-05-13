#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if char.isalpha() and char.islower():
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
