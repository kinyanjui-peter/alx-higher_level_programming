#!/usr/bin/python3
#def element_at(my_list, idx):
#    if idx < 0 or idx >= len(my_list):
#        print("None")
#    else:
##!/usr/bin/python3
# 1-element_at.py
# Brennan D Baraban <375@holbertonschool.com>


def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])

#idx = int(input("enter the index: "))
#my_list = [1, 2, 3, 4, 5]
#element_at(my_list, idx)
