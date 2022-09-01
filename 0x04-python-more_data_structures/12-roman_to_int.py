#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    index = 0
    diffSum = 0
    valueSum = 0
    try:
        length = len(roman_string)
        while index < length:
            if index + 1 < length:
                key = roman_string[index]
                nextKey = roman_string[index + 1]
                if dic[key] < dic[nextKey]:
                    diffSum += dic[nextKey] - dic[key]
                    index += 2
            if index < length:
                key = roman_string[index]
                if index + 1 < length:
                    nextKey = roman_string[index + 1]
                valueSum += dic[key]
            index += 1
        integer = diffSum + valueSum
        return integer
    except TypeError:
        return 0
