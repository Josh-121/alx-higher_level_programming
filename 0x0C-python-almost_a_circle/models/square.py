#!/usr/bin/python3
"""
The Square class module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inherits from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        defines class constuctor,calls parent constructor
        and checks input values
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        returns size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets size value
        """
        self.width = value
        self.height = value

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
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                else:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                else:
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
        returns dictionary representation of object
        """
        dict_rep = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
           }
        return dict_rep

    def __str__(self):
        """
        returns specified string representation of objects
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
