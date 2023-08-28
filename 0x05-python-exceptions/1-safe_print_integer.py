#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer using the "{:d}".format() method.

    Args:
        value (int): The integer to be printed.

    Returns:
        bool: Returns True if printing is successful,
        False if TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
