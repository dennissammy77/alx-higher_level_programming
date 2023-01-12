#!/usr/bin/python3
# 7-base_geometry.py
# Dennis Sammy
"""Defines a class BaseGeometry."""


class BaseGeometry():
    """Represents a base geometry."""

    def area(self):
        """To be Implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates type of value.

        Args:
            value (any): provided value to be determined.
            name: a string.

        Returns:
            raises a TypeError if value is not an integer with the message, <name> must be an integer,
            raises a ValueError if value is less or equal to 0 with the message, <name> must be greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
