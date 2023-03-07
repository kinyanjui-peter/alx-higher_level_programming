#!/usr/bin/python3
# Prints possible combination between 0 to 89
for i in range(0, 90):
    if i != 10 and i != 89:
        for x in range(i + 1, 10):
            print("{}{}, ".format(i, x), end="")
    if i == 89:
        print("{}\n".format(i, x))
