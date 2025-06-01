#!/usr/bin/python3
"""Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    from the specified class (directly or indirectly).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
