#!/usr/bin/python3
for num in range(0, 10):
    for x in range(num + 1, 10):
        if num != x:
            if (num == 8) and (x == 9):
                print("{}{}". format(num, x), end="\n")
                break
            print("{}{}". format(num, x), end=", ")
    num += 1
