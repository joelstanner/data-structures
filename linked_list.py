"""This module creates the functionality of a linked list data structure.
find more information at http://en.wikipedia.org/wiki/Linked_list
"""

from __future__ import unicode_literals


class LinkedList(object):
    """Methods to manipulate the linked list data"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        pointer = self.head
        printout = "("

        while pointer:
            if type(pointer.val) == unicode:
                printout += "'{}'".format(pointer.val)
            else:
                printout += "{}".format(pointer.val)
            pointer = pointer.next
            if pointer:
                printout += ", "

        printout += ")"

        return printout

    def insert(self, val):
        """insert the value 'val' at the head of the list"""
        self.head = Node(val, self.head)

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        oldHead = self.head
        try:
            self.head = self.head.next
        except AttributeError:
            raise ValueError

        return oldHead.val

    def size(self):
        """Return the length of the list"""
        counter = 0
        pointer = self.head

        while pointer:
            pointer = pointer.next
            counter += 1

        return counter

    def search(self, val):
        """Return the node containing 'val' in the list, if present, else None"""
        pointer = self.head

        if pointer.val == val:
            return pointer

        while pointer:
            if pointer.val == val:
                return pointer

            pointer = pointer.next

        return None

    def remove(self, node):
        """Remove the given node from the list, wherever it might be (node must
        be an item in the list)"""
        pointer = self.head

        # is node the first item?
        if pointer is node:
            self.head = pointer.next
            return

        while pointer.next:
            if pointer.next is node:
                pointer.next = pointer.next.next
                return

            pointer = pointer.next

    def display(self):
        """print the list represented as a Python tuple literal"""
        print self.__str__()


class Node(object):
    """Create a node object to add into the linked list"""

    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode
