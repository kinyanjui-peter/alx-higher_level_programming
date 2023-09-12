#!/usr/bin/python3
# 10-square.py
"""Define a Rectangle subclass Square."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """
        Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns area of a squar
        """
        return self.__size ** 2
