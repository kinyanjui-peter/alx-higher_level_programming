#!/usr/bin/python3
"""
    reads a text file (UTF-8) and prints it to stdout
    args:
        filename: hold the name of the file to be read
    """


def read_file(filename=""):
    """
     use the with statement
     """
    try:
        with open(filename, encoding='UTF8', mode='r') as file:
            file.seek(0)
            line = file.read()
            print(line, end="")
            """
            file not found error
            """
    except FileNotFound:
        print(f"File *'{filename}' not found.")
    except exception as e:
        print(f" Error occured")
