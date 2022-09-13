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
