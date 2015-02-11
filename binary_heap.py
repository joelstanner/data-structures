# -*- coding: utf-8 -*-
import pytest


class BinaryHeap(object):
    """Implement a binary heap data structure"""

    def __init__(self, an_iter=None):
        self._list = []

        if an_iter:
            for val in an_iter:
                self.push(val)


    def push(self, val):
        self._list.append(val)
        child_pos = len(self._list) - 1
      
        while child_pos and self._list[child_pos] > self._list[(child_pos - 1) // 2]:
            print self._list
            # swap parent and child
            self._switch(child_pos)
            child_pos = (child_pos - 1) // 2


    def pop(self):
        pass

    def _switch(self, child_index):
        """swap the parent and child"""
        parent_index = (child_index - 1) // 2

        self._list[parent_index], self._list[child_index] = (
            self._list[child_index], self._list[parent_index]
        )


