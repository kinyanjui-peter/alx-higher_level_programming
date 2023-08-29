#!/usr/bin/python3
""" square - is a class that defines a square"""


class Square:
    """object instantiation for the object square"""
    def __init__(self, size=0):
        """args:
                size: the size of square"""
        self.size = size
        @property
        def size(self):
            return self._size
        @size.setter
        def size(self, value):
            if not(isinstance(size, int)):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
                """calculate the square of an area"""
            self._size = value

    def area(self):
        return self.size ** 2
