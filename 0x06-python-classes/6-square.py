#!/usr/bin/python3
# 6-square.py
# Dennis Sammy
"""Defines a square class."""


class Square:
    """Representing a class"""
    def __init__(self, size=0, position=(0, 0)):
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
            self.__position = position

    def area(self):
        """class to calculate area of square:

        Args:
            size (int): size of square.

        Returns:
            area: current square area.
        """
        res = self.__size ** 2
        return (res)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of private attribute"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif value < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with #
        
        Args:
            size (int): size of square
        """
        if self.__size == 0:
            print()
        else:
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        """getter of square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the position"""
        if (len(value) != 2) or (type(value) is not int) or (type(value[0]) is not int) or (type(value[1]) is not int) or (value[0] < 0) or (value[1] < 0):
            raise (TypeError("position must be a tuple of 2 positive integers"))
        else:
            self.__position = value
