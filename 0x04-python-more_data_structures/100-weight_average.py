#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    weightSum = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sum += i[0] * i[1]
        weightSum += i[1]
    average = sum / weightSum
    return average
