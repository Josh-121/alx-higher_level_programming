#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for key in a_dictionary:
        max = a_dictionary[key]
        maxKey = key
        break
    for i in a_dictionary:
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            maxKey = i
    return maxKey
