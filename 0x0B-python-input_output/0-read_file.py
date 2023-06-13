#!/usr/bin/python3

'''
Write a function that reads a text file (UTF8) and prints it to stdout:
'''


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
