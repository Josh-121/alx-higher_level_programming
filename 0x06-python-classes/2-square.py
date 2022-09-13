#!/usr/bin/python3
"""
contains a class:square
"""


class Square:
    """
    The square class holding only a constructor
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
