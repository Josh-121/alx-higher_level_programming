#!/usr/bin/python3
"""
The class constructor initializing the private property: __size
"""


import string


class Node:
    """
    The class constructor initializing the private property: __size
    """
    def __init__(self, data, next_node=None):
        """
        The class constructor initializing the private property: __size
        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if type(next_node) != Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """
        The class constructor initializing the private property: __size
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        The class constructor initializing the private property: __size
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        The class constructor initializing the private property: __size
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        The class constructor initializing the private property: __size
        """
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    The class constructor initializing the private property: __size
    """
    def __init__(self):
        """
        The class constructor initializing the private property: __size
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        The class constructor initializing the private property: __size
        """
        if self.__head is None:
            self.__head = Node(value, None)
        else:
            node = Node(value, None)
            runner = self.__head
            temp = None
            while runner is not None:
                if node.data >= runner.data:
                    temp = runner
                runner = runner.next_node
            if temp is None:
                node.next_node = self.__head
                self.__head = node
            else:
                node.next_node = temp.next_node
                temp.next_node = node

    def __str__(self) -> str:
        out = ""
        runner = self.__head
        while runner is not None:
            out += (str(runner.data) + "\n")
            runner = runner.next_node
        out = out[:-1]
        return out
