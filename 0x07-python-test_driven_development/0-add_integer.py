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
        a = int(a)
        b = int(b)

    return a + b
