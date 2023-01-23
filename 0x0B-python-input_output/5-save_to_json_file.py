#!/usr/bin/python3
# 5-save_to_json_file.py
# Dennis Sammy
"""Defines a script to write a json representation of an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Saves an Object to a UTF8 text file as a json representation.
    
    Args:
        my_obj: object to be serialized.
        filename: name of file object to be added to.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
