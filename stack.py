# -*- coding: utf-8 -*-

class Stack(object):
    """Implements a stack data structure"""
    
    def __init__(self):
        self.top = None
        
    def push(self, data):
        """Take a data element and put it on the top of the stack"""
        self.top = data

    def pop(self):
        """Remove the top item from the stack, and return the value of it"""
        pass


class Item(object):
    """Wrapper for a data item that get pushed on the stack"""
    
    def __init__(self, data, next_item=None):
        self.data = data
