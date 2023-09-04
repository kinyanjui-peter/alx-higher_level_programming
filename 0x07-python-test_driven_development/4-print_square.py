#!/usr.bin/python3
"""
function that prints a square with the character #
args:
    size (int): the size of square
"""
def print_square(size):
    # size must be an integer
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    #size must be greater than 0
    if size < 0:
       raise ValueError('size must be >= 0')

    #check if its float and less than 0
    if type(size) is float and size < 0:
       raise TypeError('size must be an integer')

    #print square using #

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
