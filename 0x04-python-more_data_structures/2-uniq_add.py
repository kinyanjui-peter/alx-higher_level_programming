#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    unique_list = list(my_set)
    total = sum(unique_list)
    return total
