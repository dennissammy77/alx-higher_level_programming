#!/usr/bin/python3
# 5-base_geometry.py
# Dennis Sammy
"""Defines a Rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square class inheriting Rectangle class."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
