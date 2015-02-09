# -*- coding: utf-8 -*-


class Queue(object):

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, val):
        """Take item value, add to the back of the queue"""
        new_item = Item(val)
        try:
            self.back.next_item = new_item
        except AttributeError:
            self.front = new_item
        self.back = new_item

    def dequeue(self):
        """Remove the front item from the queue and return its value"""
        pass


class Item(object):

    def __init__(self, val, next_item=None):
        self.val = val
        self.next_item = next_item
