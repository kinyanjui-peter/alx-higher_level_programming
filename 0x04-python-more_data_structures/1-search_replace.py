#!/usr/bin/python3
#my_list - initial list
#search - element to replace the list
#replace - new element
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
