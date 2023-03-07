#!/usr/bin/python3
# Prints numbers 0 to 99
for i in range(0, 100):
    if i != 99:
        print("{:02}, ".format(i), end="")
print("{:02}\n".format(i), end="")
