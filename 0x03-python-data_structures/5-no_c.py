#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        str += char
    return str
