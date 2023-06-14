#!/usr/bin/python3
"""A class Mylist that inherits from list"""

class MyList(list):
    """Class that inherits from list

    Args:
        list: list to sort in ascending order
    """
    def print_sorted(self):
        """Prints a list in ascending order.
        """
        list_ = self[:]
        list_.sort()
        print(list_)
