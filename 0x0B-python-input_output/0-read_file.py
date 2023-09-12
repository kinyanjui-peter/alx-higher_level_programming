#!/usr/bin/python3
"""
    reads a text file (UTF8) and prints it to stdout
    args:
        filename: hold the name of the file to be read
    """


def read_file(filename=""):
    """
     use the with statement
     """
    with open(filename, encoding='UTF8',mode='r') as file:
        file.seek(0)
        print(file.read())
