#!/usr/bin/python3
"""Defining a Node class"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Instantiation

        Args:
            data (int): the data of the node
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retreive data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retreive next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set next_node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            p = self.__head
            while (p.next_node is not None and p.next_node.data < value):
                p = p.next_node
            new.next_node = p.next_node
            p.next_node = new

    def __str__(self):
        my_list = []
        p = self.__head
        while p is not None:
            my_list.append(str(p.data))
            p = p.next_node
        return ('\n'.join(my_list))
