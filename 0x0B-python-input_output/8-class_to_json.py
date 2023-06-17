#!/usr/bin/python3
"""Module with the function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of an object."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure,
    (list, dictionary, string, integer and boolean) for JSON serialization,
    of an object.

    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """
    return obj.__dict__
