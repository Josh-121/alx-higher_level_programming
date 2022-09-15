#!/usr/bin/python3
"""
Contains the Node and SinglyLinked class
"""


class Node:
    """
    contains a constructor,properties getters and setters
    """
    def __init__(self, data, next_node=None):
        """
        Initializes input data and next Node and handles
        input errors
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
        gets the __data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets the __data attribute
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        gets the __next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets the __next_node attribute
        """
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Contains the class constructor,sorted_insert method and the
    __str__ method
    """
    def __init__(self):
        """
        initializing head
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts data in the list due to it's sorted position.
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
        """
        returns the linked list in str format
        """
        out = ""
        runner = self.__head
        while runner is not None:
            out += (str(runner.data) + "\n")
            runner = runner.next_node
        out = out[:-1]
        return out
