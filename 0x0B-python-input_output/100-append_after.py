#!/usr/bin/python3
# 100-append_after.py
# Dennis Sammy
"""Defines an insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a string.

    Args:
        filename: name of file.
        search_string: string to search for in the file.
        new_string: The string to be inserted.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode='w', encoding='utf-8') as nf:
        nf.write(text)
