#!/usr/bin/python3
""" function that returns True if the object is exactly

    an instance of the specified class Otherwise False.
"""


def is_same_class(obj, a_class):
    """function that checks if object is an instance of a class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
