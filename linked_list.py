class LinkedList(object):
    """docstring for LinkedList"""

    def __init__(self):
        self.head = None

    def __str__(self):
        counter = 0
        pointer = self.head
        printout = "("

        # 1st object case
        if pointer:
            counter += 1
            printout += "{}, '{}'".format(counter, pointer.val)

        while pointer.next:
            counter += 1
            printout += ", {}, '{}'".format(counter, pointer.next.val)
            pointer = pointer.next

        printout += ")"

        return printout

    def insert(self, val):
        self.head = Node(val, self.head)

    def pop(self):
        oldHead = self.head
        try:
            self.head = self.head.next
        except AttributeError:
            return None

        return oldHead.val

    def size(self):
        counter = 0
        pointer = self.head

        if pointer:
            counter += 1

            while pointer.next:
                pointer = pointer.next
                counter += 1

        return counter

    def search(self, val):
        pointer = self.head

        if pointer.val == val:
            return pointer

        while pointer.next:
            if pointer.next.val == val:
                return pointer.next

            pointer = pointer.next

        return None

    def remove(self, node):
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
        print self.__str__()


class Node(object):

    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode
