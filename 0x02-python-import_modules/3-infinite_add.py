#!/usr/bin/python3
def add_values(argv):
    count = 0
    for i in range(len(argv)):
        count += 1
    sum_val = 0
    idx = 1
    while count != 1:
        sum_val += int(argv[idx])
        idx += 1
        count -= 1
    print(sum_val)


if __name__ == "__main__":
    import sys
    add_values(sys.argv)