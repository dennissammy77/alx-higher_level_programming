#!/usr/bin/python3
# 1-mylist.py
# Dennis Sammy
"""Defines an inherited list class from MyList."""



class MyList(list):
    """Implemnts a sorted printing for list class."""

    def print_sorted(self):
        """Print a list in a sorted ascending order."""
        print(sorted(self))
