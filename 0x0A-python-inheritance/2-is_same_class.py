#!/usr/bin/python3
"""Defines a function is_same_class()."""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.

    Args:
        obj: object to check type.
        a_class: type to check.

    Returns:
        boolean: True or False.
    """
    return type(obj) == a_class
