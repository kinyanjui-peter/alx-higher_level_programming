#!/usr/bin/python3
for num in range(0, 8):
    for x in range(num + 1, 10):
#        if num != x:
#            if (num == 8) and (x == 9):
        print("{:d}{:d}". format(num, x), end=", ")
#                break
print("{:d}{:d}". format(num + 1, x))
#    num += 1

