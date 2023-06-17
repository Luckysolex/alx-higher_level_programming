#!/usr/bin/python3
"""Module with the function to return a JSON data."""


def to_json_string(my_obj):
    """Function to return JSON representation of an object.

    Args:
        my_obj: Object to be passed.

    Returns:
        str: JSON representation of my_obj
    """
    # serialising json
    return json.dumps(my_obj)
