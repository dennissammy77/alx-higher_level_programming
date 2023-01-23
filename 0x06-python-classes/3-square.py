#!/usr/bin/python3
# 3-sqaure.py
# Dennis Sammy
"""Defines a square class."""


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

    def area(self):
        """class to calculate area of square:

        Args:
            size (int): size of square.

        Returns:
            area: current square area.
        """
        res = self.__size ** 2
        return (res)
