#!/usr/bin/python3
"""
The class constructor initializing the private property: __size
"""


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
            self.__head = Node(self.value, None)
        node = Node(self.value, None)
        while self.__head.next_node is not None:
            if self.__head.data <= node.data:
                node.next_node = self.__head.next_node
                self.__head.next_node = node
            self.__head = self.__head.next_node
        if self.__head.next_node is None:
            node.next_node = self.__head.next_node
            self.__head.next_node = node
