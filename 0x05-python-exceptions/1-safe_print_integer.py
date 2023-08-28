#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer using the "{:d}".format() method.

    Args:
        value (int): The integer to be printed.

    Returns:
        bool: Returns True if printing is successful, False if TypeError or ValueError occurs.
    """
    try:
        # Try to format and print the integer value
        print("{:d}".format(value))

        # Return True to indicate successful printing
        return True
    except (TypeError, ValueError):
        # Handle exceptions (TypeError and ValueError) that might occur during formatting
        # Return False to indicate that printing failed due to an exception
        return False
