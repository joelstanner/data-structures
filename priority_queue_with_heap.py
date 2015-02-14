from binary_heap import BinaryHeap


class PriorityQueue(object):

    def __init__(self):
        self.heap = BinaryHeap()
        self.seniority = 0

    def insert(self, priority, val):
        self.heap.push((priority, self.seniority, val))
        self.seniority -= 1

    def pop(self):
        try:
            return self.heap.pop()[2]
        except IndexError:
            raise IndexError("The queue is empty")

    def peek(self):
        try:
            return self.heap._list[0][2]
        except IndexError:
            raise IndexError("The queue is empty")
