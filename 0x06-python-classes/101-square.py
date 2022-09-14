#!/usr/bin/python3
"""
contains the square class
"""


class Square:
    """
    contains constructor,area method,getter,setter and my_print method
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The class constructor initializing the private properties: __size
        and __position
        """
        for i in position:
            if type(i) != int or i < 0 or len(position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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

    @property
    def position(self):
        """
        gets the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position attribute
        """
        for i in value:
            if type(i) != int or i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates and returns the area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")
        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self) -> str:
        """
        returns the square in str format
        """
        self.squareStr = ""
        if self.__size == 0:
            self.squareStr += "\n"
            return

        for i in range(self.__position[1]):
            self.squareStr += "\n"
        for x in range(self.__size):
            for y in range(self.__position[0]):
                self.squareStr += " "
            for z in range(self.__size):
                self.squareStr += "#"
            self.squareStr += "\n"
        self.squareStr = self.squareStr[:-1]
        return self.squareStr
