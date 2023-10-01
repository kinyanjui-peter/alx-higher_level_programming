#!/usr/bin/python3
"""
    Module to find the maximum integer in a list
    """
def max_integer(list=[]):
    """
        Function to find and return the maximum integer in a list of integers
        If the list is empty, the function returns None
        """

    if len(list) == 0:
        """ check list length"""
        return None
    res = list[0]
    xi = 1
    while x < len(list):
        if list[x] > res:
            res = list[x]
        x += 1
    return res
