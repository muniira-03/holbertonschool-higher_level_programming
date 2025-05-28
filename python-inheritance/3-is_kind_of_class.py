#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """checks if object is instance of a class that inherited from a_class
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
