#!/usr/bin/python3
"""Module for text_identation method."""


def text_identation(text):
    """Method for adding 2 new lines after '.?:' characters.

    Args:
        text: The str text.

    Raises:
        TypeError: if text is not a STR.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_identation.txt")
