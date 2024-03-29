#!/usr/bin/python3
"""Defines a function inherits_from()."""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from
    the specified class ; otherwise False.

    Args:
        obj: object to be checked.
        a_class: type of type to check.

    Returns:
        boolean: True or False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
