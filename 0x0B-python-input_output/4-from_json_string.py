#!/usr/bin/python3
# 4-from_json_string.py
# Dennis Sammy
"""Deserializes a json representation."""
import json

def from_json_string(my_str):
    """converts a json string back to an object.
    
    Args:
        my_str (str): string to be deserializes.
    Returns:
        an Object.
    """
    return json.loads(my_str)
