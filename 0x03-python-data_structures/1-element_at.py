#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
      print("None")
    print(f"{my_list[idx]}")

idx = int(input("enter the index: "))
my_list = [1, 2, 3, 4, 5]
element_at(my_list, idx)
