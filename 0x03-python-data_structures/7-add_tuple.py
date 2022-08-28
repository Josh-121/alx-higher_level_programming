#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newlist = []
    tuple_a_list = list(tuple_a)
    tuple_b_list = list(tuple_b)
    i = 0
    while i < 2:
        if len(tuple_a_list) < 2:
            tuple_a_list.append(0)
        if len(tuple_b_list) < 2:
            tuple_b_list.append(0)
        newlist.append(tuple_a_list[i] + tuple_b_list[i])
        i += 1
    return tuple(newlist)
