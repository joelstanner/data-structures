# -*- coding: utf-8 -*-


class Queue(object):
    """Implement a queue data structure"""
    def __init__(self):
        self.front = None
        self.back = None

    def __iter__(self):
        current = self.front
        while current:
            yield current
            current = current.next_item

    def enqueue(self, val):
        """Take item value, add to the back of the queue"""
        # new_item = Item(val)
        try:
            self.back = self.back.next_item = Item(val)
            print "back: {}, back next item: {}".format(self.back, self.back.next_item)
        except AttributeError:
            self.back = self.front = Item(val)
            print "back: {}, front: {}".format(self.back, self.front)
        #self.back = new_item

    def dequeue(self):
        """Remove the front item from the queue and return its value"""

        prevFront = self.front
        try:
            self.front = self.front.next_item
        except AttributeError:
            raise AttributeError("The queue is empty")

        return prevFront.val

    def size(self):
        count = 0
        for _ in self:
            count += 1

        return count


class Item(object):

    def __init__(self, val, next_item=None):
        self.val = val
        self.next_item = next_item
