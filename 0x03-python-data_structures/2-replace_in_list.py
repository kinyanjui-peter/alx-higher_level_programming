#!/usr/bin/python3
#replace_in_list - Replaces content of a list 

def replace_in_list(my_list, idx, element):
    
    if idx >= 0 and idx < len(my_list):
        print(my_list)
        my_list[idx] = element
        print(my_list)
    return (my_list)
        
my_list = [1, 2, 3, 4, 5, 6]
idx = int(input(" please enter the index to replace: "))
element = int(input(" please enter the the new element: "))
replace_in_list(my_list, idx, element)
