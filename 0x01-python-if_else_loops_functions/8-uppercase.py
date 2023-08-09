#!/usr/bin/python3
def uppercase(str):
    upperletter = ""
    for i in str:
        if (97 <= ord(i) <= 122):
            upperletter = chr(ord(i) - 32)
        else:
            upperletter = i;
        print("{}". format(upperletter), end="")
    print()
