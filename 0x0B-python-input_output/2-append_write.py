#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    args:
        @filename: filename passed
        @text: text file to be appended
    """

def append_write(filename="", text=""):
    """error handling"""
    try:
        with open(filename, encoding='utf-8', mode ='a+') as file:
            appended_file = file.append(text)
            char_added = len(text)
            return char_added
    except Exception as e:
        return 0
