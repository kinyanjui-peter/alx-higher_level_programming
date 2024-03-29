#!/usr/bin/python3
"""
a function that prints my first name and last name
"""
def say_my_name(first_name, last_name=""):
    #first and last name should be string
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {}, {}".format(first_name, last_name))
