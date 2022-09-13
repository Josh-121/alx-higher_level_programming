#!/usr/bin/python3
"""
contains the square class
"""


class Square:
    """
    The Square class holding a constructor and an area method
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
