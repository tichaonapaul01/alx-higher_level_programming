#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Function that returns True/False

    Args:
        obj: object
        a_class: class type

    Returns:
        True
        False
    """
    return type(obj) is a_class
