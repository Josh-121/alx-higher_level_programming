#!/usr/bin/python3
"""
contains the square class
"""


class Square:
    """
    contains constructor,area method,getter and setter
    """
    def __init__(self, size=0):
        """
        The class constructor initializing the private property: __size and
        handling input errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates and returns the area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        gets the size attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the size attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
