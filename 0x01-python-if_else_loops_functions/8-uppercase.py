#!/usr/bin/python3
def uppercase(str1):
    upperletter = ""
    for i in str1:
        if (97 <= ord(i) <= 122):
            upperletter += chr(ord(i) - 32)
        else:
            upperletter += i;
    return upperletter

