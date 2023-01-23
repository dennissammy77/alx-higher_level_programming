#!/usr/bin/python3
# 3-to_json_string.py
# Dennis Sammy

import json
"""Defines a JSON respresentation of an object."""

def to_json_string(my_obj):
    """Serializes an object to Json.

    Args:
        my_obj: object to be serialized.
    Returns:
        json representation of an object.
    """
    return json.dumps(my_obj)
