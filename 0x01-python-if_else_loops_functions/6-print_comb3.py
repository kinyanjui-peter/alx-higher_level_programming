#!/usr/bin/python3
# Prints possibl combination between 0 to 89
for i in range(0, 10):
    for x in range(i + 1, 10):
        if i != 8 and i != 9:
            print("{}{}, ".format(i, x), end="")
        else:
            print("{}{}".format(i, x))
