#!/usr/bin/python3
from magic_calc import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for xx in range(4, 6):
            c = add(c, xx)
        return (c)
    else:
        return (sub(a, b))
