#!/usr/bin/python3

def upper(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            nxt = chr(ord(str[i]) - 32)
            print("{}".format(nxt), end="")
        else:
            print("{}".format(str[i]), end="")
