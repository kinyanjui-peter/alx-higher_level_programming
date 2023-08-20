#!/usr/bin/python3
#my_list - initial list
#search - element to replace the list
#replace - new element
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            replace = search
            print(replace)
        else:
            print(i)

