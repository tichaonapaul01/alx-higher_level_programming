#!/usr/bin/python3
"""
===================================
Module with the method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """
    Method that returns True if an object is an instance of a class
    that is inherited from another class.

    Args:
        obj: The object to check.
        a_class: The class type to compare against.

    Returns:
        True if obj is an instance of a class that is inherited from a_class.
        False otherwise.
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
