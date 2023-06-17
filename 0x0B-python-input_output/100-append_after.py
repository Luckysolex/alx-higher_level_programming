#!/usr/bin/python3
"""Module with the append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: name of the file
        search_string: string to be searched
        new_string: New text string to be inserted
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as t:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        t.write(s)
