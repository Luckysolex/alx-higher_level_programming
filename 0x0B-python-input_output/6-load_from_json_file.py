#!/usr/bin/python3
"""Module with the load_from_json function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str): name of the file.

    Returns:
        object: object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
