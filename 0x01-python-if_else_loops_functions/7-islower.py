#!/usr/bin/python3

def islower(c):
    if c >= 'a' and c <= 'z':
        return True
    else:
        return False


name = input("Enter a character: ")
print(islower(name))
