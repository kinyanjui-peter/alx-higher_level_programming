#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = 0
    sorted_dict = sorted(a_dictionary.keys())
    for key in sorted_dict:
        value = a_dictionary[key]
        print(f"{key}: {value}")
