#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
        """
def text_indentation(text):
    """
    Args:
        text (str): text
    Raise
        TypeError: when text is not str
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(f"{text}", end="")
