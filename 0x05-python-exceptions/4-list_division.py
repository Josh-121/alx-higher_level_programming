#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    index = 0
    ratio = 0
    while index < list_length:
        try:
            ratio = my_list_1[index] / my_list_2[index]
            newList.append(ratio)
        except ZeroDivisionError:
            newList.append(0)
            print("division by 0")
        except TypeError:
            newList.append(0)
            print("wrong type")
        except IndexError:
            newList.append(0)
            print("out of range")
        finally:
            index += 1
    return newList
