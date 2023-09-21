#!/usr/bin/python3
"""
An empty class that defines a rectangle
"""


class Rectangle:
    """
    Docstring for my class
    the class performs various function like str, are a etc
    Attributes:
        widthe(int): widthe of the rectangle
        height(int): height of the recrangle
    """
    number_of_instances = 0
    """
    assignment of width and height of a rectangle
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 and self._height == 0:
            return 0
        else:
            return (self._width + self._height) * 2
        # print a reactangle of height and length indicated

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self._height):
                rectangle_str += "#" * self._width + "\n"
            return rectangle_str

    def __repr__(self):
        return f'Rectangle({self._width}, {self._height})'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
