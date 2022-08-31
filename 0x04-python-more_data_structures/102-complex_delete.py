#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delkeyList = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delkeyList.append(key)
    for key in delkeyList:
        a_dictionary.pop(key)
    return a_dictionary
