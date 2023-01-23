#!/usr/bin/python3
# 1-square.py
# Dennis Sammy
"""Define a square class."""


class Square:
    """Represent a square"""

    def __init__(self, square_size):
        """Initialize a new square

        Args:
            size (int): Size of a new square.
        """
        self.__size = square_size
