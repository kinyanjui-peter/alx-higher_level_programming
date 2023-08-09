#!/usr/bin/python3
def pow(a, b):
    mul = 1
    for i in range(b):
        mul *= a
    for i in range(-b):
        mul /= a
    return mul
