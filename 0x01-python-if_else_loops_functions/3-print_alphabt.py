#!/usr/bin/python3
for char in range(97, 123):
    character = chr(char)
    if character not in ['e' , 'q' ]:
        print("{:s}" .format(character), end="")
