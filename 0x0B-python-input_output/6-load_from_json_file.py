#!/usr/bin/python3
# 6-load_from_json_file.py
# Dennis Sammy
"""Defines a script that creates an object from a json file."""
import json

def load_from_json_file(filename):
    """Deserializes a json file.
    
    Args:
        filename: name of file to be deserialized.
    """
    with open(filename, encoding='utf-8') as f:
        obj = json.load(f)
        return obj
