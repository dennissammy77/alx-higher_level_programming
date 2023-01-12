#!/usr/bin/python3
# 100-my_int.py
# Dennis Sammy
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts int operators == and !=."""

    def __equal__(self, value):
        """Converts == to != ."""
        return self.real != value

    def __not_equal__(self, value):
        """converts != to == ."""
        return self.real == value
