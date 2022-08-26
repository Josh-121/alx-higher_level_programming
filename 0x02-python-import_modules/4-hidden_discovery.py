#!/usr/bin/python3
def discovr():
    for name in dir(hidden_4):
        if not (name[0] == '-' and name[1] == '-'):
            print(name)


if __name__ == "__main__":
    import hidden_4
    discovr()