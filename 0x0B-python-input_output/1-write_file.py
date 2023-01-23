#!/usr/bin/python3
# 1-write_file.py
# Dennis Sammy
"""Defines a writing function to a file."""


def write_file (filename="", text=""):
    """Write a string to a UTF8 text file.
    
    Args:
        filename: name of file to write.
        text (str): string to write to the file.

    Returns:
        Number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
