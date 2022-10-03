#!/usr/bin/python3
"""
The Rectangle class module
"""

from base import Base


class Rectangle(Base):
    """
    inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        defines class constuctor,calls parent constructor
        and checks input values
        """
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """
        returns width value
        """
        return self.__width

    @property
    def height(self):
        """
        returns height value
        """
        return self.__height

    @property
    def x(self):
        """
        returns x value
        """
        return self.__x

    @property
    def y(self):
        """
        returns y value
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        sets width value
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """
        sets height value
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """
        sets x value
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """
        sets y value
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        returns area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        displays visual representation of rectangle object
        """
        print("\n" * self.y, end="")
        str = " " * self.x
        for i in range(self.__height):
            print(str, end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """
        updates objects properties
        """
        if args:
            length = len(args)
            for i in range(length):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                else:
                    self.__y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                else:
                    self.__y = kwargs[key]

    def to_dictionary(self):
        """
        returns dictionary representation of object
        """
        dict_rep = {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
            }
        return dict_rep

    def __str__(self):
        """
        returns specified string representation of objects
        """
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
            )
            )
