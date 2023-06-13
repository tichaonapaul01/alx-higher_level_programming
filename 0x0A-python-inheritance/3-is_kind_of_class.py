#!/usr/bin/python3
"""
===================================
Module with the method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """
    Method that returns True if an object is an instance of a class
    or an instance of a subclass.

    Args:
        obj: The object to check.
        a_class: The class type to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass.
        False otherwise.
    """
    return isinstance(obj, a_class)
