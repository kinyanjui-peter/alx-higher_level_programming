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
    Raises:
        TypeError: in case the arguments are not int or float

    Return:
        (int) : Sum of the int a and b
        """
   if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return b
    return int(a) + int(b)
