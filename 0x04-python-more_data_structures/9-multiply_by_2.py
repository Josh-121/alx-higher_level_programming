#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = {}
    for key in a_dictionary:
        newDic[key] = a_dictionary[key]
    for i in newDic:
        newDic[i] = 2 * newDic[i]
    return newDic
