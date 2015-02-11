# -*- coding: utf-8 -*-


class Binaryheap(object):
    """Implement a binary heap data structure"""

    def __init__(self):
        self._list = []

    def push(self, val):
        self._list.append(val)
        child_pos = len(self._list) - 1
        parent_pos = (child_pos - 1) // 2

        while child_pos and self._list[child_pos] > self._list[parent_pos]:
            # swap parent and child
            self._switch(child_pos)
            child_pos = parent_pos

    def pop(self):
        pass

    def _switch(self, child_index):
        """swap the parent and child"""
        parent_index = (child_index - 1) // 2

        self._list[parent_index], self._list[child_index] = (
            self._list[child_index], self._list[parent_index]
        )


