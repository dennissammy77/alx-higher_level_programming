#!/usr/bin/python3
# 4-inherits_from.py
# Dennis Sammy
"""Defines an instance checking function."""


def inherits_from(obj, a_class):
    """Checks if an obj is an instance of a class that is directly/indirectly inherited from a specified class.

    Args:
        obj (any): object to check.
        a_class (type): class provided to be cross ref.

    Returns:
        True- if obj is an instance of a_class,
        Otherwise it returns False.
    """
    if issubclass(type(obj), a_class) and type(obj != a_class):
        return True
    return False
