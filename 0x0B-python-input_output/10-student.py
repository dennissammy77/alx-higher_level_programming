#!/usr/bin/python3
# 9-student.py
# Dennis Sammy
"""Defines a Student class."""


class Student:
    """Defines a student class."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new student.
        
        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets a dictionary representation of the student.

        if attr is a list of strings, it represents only those attr included in the list.

        Args:
            attrs:the attributes to represent.
        """
        if (type(attrs) == list) and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
