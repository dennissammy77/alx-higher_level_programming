#!/usr/bin/python3
# 0-lookup.py
# Dennis Sammy
""" Defines a function that returns the list of available attributes and methods of an object."""


def lookup(obj):
    """Return a list of an objects available attr."""
    return(dir(obj))
