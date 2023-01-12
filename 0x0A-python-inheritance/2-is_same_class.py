#!/usr/bin/python3
# 2-is_same_class.py
# Dennis Sammy
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    """Checks an object if it is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): the class to match the type of obj to.

    Returns:
        True if obj is same as instance of a_class.
        Otherwise returns False.
    """
    if type(obj) == a_class:
        return True
    return False
