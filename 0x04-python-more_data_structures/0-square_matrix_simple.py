#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newList = []
    squareList = []
    for i in matrix:
        for j in i:
            squareList.append(j ** 2)
        newList.append(squareList)
        squareList = []
    return newList
