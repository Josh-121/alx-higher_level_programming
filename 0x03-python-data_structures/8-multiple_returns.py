#!/usr/bin/python3
def multiple_returns(sentence):
    list = []
    count = len(sentence)

    list.append(count)
    if count > 0:
        list.append(sentence[0])
    else:
        list.append(None)
    return tuple(list)
