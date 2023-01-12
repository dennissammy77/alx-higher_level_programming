#!/usr/bin/python3
# 9-rectangle.py
# Dennis Sammy
"""Defines a class Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """inherits from the base geometry class."""

    def __init__(self, width, height):
        """initializes a new rectangle.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
    
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
