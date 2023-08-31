#!/usr/bin/python3
""" square - is a class that defines a square"""


class Square:
    """object instantiation for the object square"""
    def __init__(self, size=0, position = (0, 0)):
        """args:
                size: the size of square"""
        self._size = size

        @property
        def size(self):
            return self._size

        @size.setter
        def size(self, value):
            if not(isinstance(size, int)):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
                """calculate the square of an area"""
            self._size = value
        @property
        @position.getter
        def position(self):
            return self._position
        @position.setter
        def position(self, value):
            if not isinstance(value, turple) or len(value) != 2:
                raise TypeError(position must be a tuple of 2 positive integers)
            if position[1] > 0:
                print("", end="")
            else:
                print(" ")

    def area(self):
        return self._size ** 2


    def my_print(self):
        if self._size == 0:
            print("")
        else:
            for i in range(self._size):
                for _ in range(self._size):
                    print("#", end="")
                print("")
