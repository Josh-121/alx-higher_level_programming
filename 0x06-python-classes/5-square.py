#!/usr/bin/python3
"""
The class constructor initializing the private property: __size
"""


class Square:
    """
    The class constructor initializing the private property: __size
    """
    def __init__(self, size=0):
        """
        The class constructor initializing the private property: __size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The class constructor initializing the private property: __size
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        The class constructor initializing the private property: __size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        The class constructor initializing the private property: __size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        The class constructor initializing the private property: __size
        """
        count = 0
        while True:
            if count == self.area():
                break
            print('#', end="")
            count += 1
            if count % self.__size == 0:
                print()
        if count == 0:
            print()
