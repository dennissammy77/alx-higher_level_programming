#!/usr/bin/python3
# 2-square.py
# Dennis Sammy
"""Defines a sqaure class."""


class Square:
    """Representing a class"""
    def __init__(self, size=0):
        """Class to create a square of size

        Args:
            size (int): size of the square.
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
