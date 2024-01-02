#!/usr/bin/python3
"""Singly Linked Lists Implementation"""


class Node:
    """Initializing Private Instances"""
    def __init__(self, data, next_node=None):
        """Private data and next node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Data Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data Setter"""
        self.__data = value

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Next Node Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Next Node Setter"""
        self.__next_node = value

        if not value == None or not value == Node:
            raise TypeError("next_node must be a Node object")



    """Singly Linked List Implementation"""


    class SinglyLinkedList:
        
