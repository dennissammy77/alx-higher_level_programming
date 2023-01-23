#!/usr/bin/python3
# 0-read_file.py
"""Defines a reading function."""


def read_file(filename=""):
    """Prints contents of UTF8 file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
