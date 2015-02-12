# -*- coding: utf-8 -*-


class BinaryHeap(object):
    """Implements a binary max-heap data structure"""

    def __init__(self, an_iter=None):
        '''Initializes the heap,
        optionally populates it with the given iterable
        '''

        self._list = []

        if an_iter:
            for val in an_iter:
                self.push(val)

    def push(self, val):
        '''Pushes the value into the heap,
         adjusting the ordering to maintain the heap
         '''

        self._list.append(val)
        child_pos = len(self._list) - 1

        while child_pos and (
                self._list[child_pos] > self._list[(child_pos - 1) // 2]):

            # swap parent and child
            self._switch(child_pos)
            child_pos = (child_pos - 1) // 2

    def pop(self):
        '''Pops the top value off the heap and returns it,
         adjusting the ordering accordingly
         '''

        try:
            self._list[0], self._list[-1] = self._list[-1], self._list[0]
            top = self._list.pop()

            parent_pos = 0
            children_pos = self._find_children(parent_pos)
            while children_pos != []:
                larger_child = None
                larger_child_index = None
                if len(children_pos) > 1:
                    if self._list[children_pos[0]] >= self._list[
                            children_pos[1]]:
                        larger_child = self._list[children_pos[0]]
                        larger_child_index = children_pos[0]
                    else:
                        larger_child = self._list[children_pos[1]]
                        larger_child_index = children_pos[1]
                else:
                    larger_child = self._list[children_pos[0]]
                    larger_child_index = children_pos[0]

                if self._list[parent_pos] < larger_child:
                    self._switch(larger_child_index)
                else:
                    break
                parent_pos = larger_child_index
                children_pos = self._find_children(parent_pos)

            return top
        except IndexError:
            raise IndexError("The heap is empty")

    def _switch(self, child_index):
        """Helper, swaps the child at the given index with its parent"""
        parent_index = (child_index - 1) // 2

        self._list[parent_index], self._list[child_index] = (
            self._list[child_index], self._list[parent_index]
        )

    def _find_children(self, parent):
        '''Helper, returns a list of children for the given parent,
         an empty list if none
         '''

        children_indices = []

        if len(self._list) > 2*parent + 1:
            children_indices.append(2*parent+1)
        if len(self._list) > 2*parent + 2:
            children_indices.append(2*parent+2)

        return children_indices
