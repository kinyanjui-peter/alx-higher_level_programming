#!/usr/bin/python3
"""safe_print_list - funtion name
my_list = array of list
x: number in list"""


def safe_print_list(my_list=[], x=0):
    count = 0

    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
