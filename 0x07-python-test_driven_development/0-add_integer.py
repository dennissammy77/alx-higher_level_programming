#!/usr/bin/python3
#0-add_integer.py
"""Defines a function to add two integers."""



def add_integer(a, b=98):
    """returns the result of the sum of two integers,  a and b.

    Float arguments are typecasted into ints before addition function.

    Raises:
        TypeError: If a or b is non integer or a non float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
