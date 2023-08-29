#!/usr/bin/python3
""" square - is a class that defines a square"""


class Square:
    """object instantiation for the object square"""
    def __init__(self, size=0):
        """args:
                size: the size of square"""
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
