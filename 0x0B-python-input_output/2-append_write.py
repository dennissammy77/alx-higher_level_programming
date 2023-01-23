#!/usr/bin/python3
# 2-append_write.py
# Dennis Sammy
"""Defines a script to append a string to a file."""

def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file.

    Args:
        filename: name of file to be worked on.
        text (str): string to be appended to the file.

    Returns:
        Number of characters needed.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
