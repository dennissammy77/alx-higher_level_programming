#!/usr/bin/python3
# 3-is_kind_of_class.py
# Dennis Sammy
"""Defines an Object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class.

    Args:
        obj: Object being checked.
        a_class: class to cross-ref to.

    Returns:
        True-if the object is an instance of a class,
        Otherwise returns False.
    """
    if isinstance(obj, a_class):
        return True
    return False
