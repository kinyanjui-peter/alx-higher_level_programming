#!/usr/bin/python3

"""
Write a class MyInt that inherits from int
"""


class MyInt(int):
    """
    A subclass of class int
    """
    def __eq__(self, unknown):
        """
        sets the behaviour of == 
        """
        return int(self) != unknown

    def __ne__(self, unknown):
        """
        sets the != behavior
        """
        return int(self) == unknown
