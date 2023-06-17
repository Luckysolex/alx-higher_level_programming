#!/usr/bin/python3
"""Module with the write_file function."""


def write_file(filename="", text=""):
    """Function that writes a string text and returns the number of characters.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number of characters written to a file."""
        return f.write(text)
