#!/usr/bin/python3
def print_args(argv):
    length = len(argv)
    if (length == 1):
        print("{0:d} arguments.".format(length - 1))
    elif (length > 1):
        if (length - 1 == 1):
            print("{0:d} argument:".format(length - 1))
        elif (length > 1):
            print("{0:d} arguments:".format(length - 1))
        for i in range(length - 1):
            print("{0:d}: {1:s}".format(i + 1, argv[i + 1]))


if __name__ == "__main__":
    import sys
    print_args(sys.argv)