#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    """ a function that findsthe largest number in alist"""
    # Initialize max_number to negative infinity
    max_number = float('-inf')
    numbers = list_of_integers
    if not list_of_integers:
        """return none of the arguent is 0"""
        return None

    # Iterate through the list of numbers
    for num in numbers:
        """Update max_number if the current number is greater
        """
        if num > max_number:
            max_number = num
    return max_number
