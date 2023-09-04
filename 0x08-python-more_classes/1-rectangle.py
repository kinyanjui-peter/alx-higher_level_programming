#!/usr/bin/python3
"""
An empty class that defines a rectangle
"""


class Rectangle:
    """
    assignment of width and height of a rectangle
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def __str__(self):
        return "{'_Rectangle__height':" + str(self._height) + ",\
                '_Rectangle__width':" + str(self._width) + "}"
