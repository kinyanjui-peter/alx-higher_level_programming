#!/usr/bin/python3
#replace_in_list - Replaces content of a list

def replace_in_list(my_list, idx, element):
    
    if idx >= 0 and idx < len(my_list):
       my_list[idx] = element
    return (my_list)
