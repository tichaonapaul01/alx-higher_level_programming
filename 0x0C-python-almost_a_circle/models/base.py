#!/usr/bin/python3
'''
base.py
'''


class Base:
    __nb_objects = 0


def __init__(self, id=None):
    self.id = None
    if id is not None:
        self.id = int(id)

    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objecs
