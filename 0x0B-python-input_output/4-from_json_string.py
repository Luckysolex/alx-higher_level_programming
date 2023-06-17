#!/usr/bin/python3
"""Module with the function to convert from JSON data to object."""
import json


def from_json_string(my_str):
    """Function that returns an object represented by a JSON data.

    Args:
        my_str: The JSON data to be returned as string

    Returns:
        object: from a JSON string.
    """
    # deserialising
    return json.loads(my_str)
