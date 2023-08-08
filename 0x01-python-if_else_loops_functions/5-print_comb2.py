#!/usr/bin/python3
for x in range(100):
#    if x == 99:
#        print("{}\n". format(x), end="")
#        break
#    print("{x:02d}, ". format(x), end="")
    print(f"{x:02d}", end=", " if x < 99 else "\n")
