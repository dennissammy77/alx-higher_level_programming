#!/usr/bin/python3
# 8-class_to_json.py
# Dennis Sammy
"""Defines a function that returns a dictionary description."""


def class_to_json(obj):
    """returns the dictionary representation of a simple data structure."""
    return obj.__dict__
