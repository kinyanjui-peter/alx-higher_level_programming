#!/usr/bin/python3
"""
   writes a string to a text file (UTF8) and returns
   the number of characters written
     """
def write_file(filename="", text=""):
    """
        use the with statement
        args:
            filename: name of the file to be opened
            text: text file to be written to
            """
    try:
        with open(filename, encoding='UTF-8', mode='w') as file:
            """
            copy string from filename to text.txt and 
            count the number of characters
            """
            file.tell()
            file.seek(0)
            char_written = file.write(text)
            return char_written
    except Exception as e:
        return 0

