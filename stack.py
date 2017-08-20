# -*- coding: utf-8 -*-


class Stack(object):
    """Implements a stack data structure"""

    def __init__(self):
        self.top = None

    def push(self, data):
        """Take a data element and put it on the top of the stack"""
        self.top = Item(data, self.top)

    def pop(self):
        """Remove the top item from the stack, and return the value of it"""
        prevTop = self.top
        try:
            self.top = self.top.next_item
        except AttributeError:
            raise ValueError("The stack is empty")

        return prevTop.data


class Item(object):
    """Wrapper for a data item that gets pushed on the stack"""

    def __init__(self, data, next_item=None):
        self.data = data
        self.next_item = next_item
