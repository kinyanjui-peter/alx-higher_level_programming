#!/usr/bin/python3
"""
    implementation of the add function
    The function adds 2 numbers a and b
    Raises:TypeError if a or b are not integers or float
    """
def add_integer(a, b=98):
    """
    return the addition of a and b
    args:
        a(int, float) the first number
        b(int, float) the second number
        """
    if not isinstance(a,(int, float)):
        raise TypeError('a imust be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float) and isinstance(b, float):
        a = int(a)
        b = int(b)

    return a + b
