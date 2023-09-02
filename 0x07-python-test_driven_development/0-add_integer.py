#!/usr/bin/python3
"""implementation of the add function"""
def add_integer(a, b=98):
    """ the function adds 2 numbers a and b
    >>> add_integer(4, 10)
    14
    >>> add_integer(4, 'School')
    Traceback (most recent call last):
        ...
    TypeError: b must be float or integers'
    >>> add_integer('School', 10)
    Traceback (most recent call last):
        ...
    TypeError: must be float or integers'
    >>> add_integer(-4, 10)
    6
    >>> add_integer(14.5, -10)
    4
        """
    if not isinstance(a,(int, float)):
        raise TypeError('a imust be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float) and isinstance(b, float):
        x = int(a)
        y = int(b)

    return x + y
