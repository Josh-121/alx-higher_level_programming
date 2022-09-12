#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    notInt = 0
    try:
        while index < x:
            if type(my_list[index]) == int:
                print("{:d}".format(my_list[index]), end="")
            else:
                notInt += 1
            index += 1
        print()
    except IndexError:
        print()
    return (index - notInt)
