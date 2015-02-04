class LinkedList(object):
    """docstring for LinkedList"""


    def __init__(self):
        self.head = None


    def __str__(self):
        pass

    def insert(self, val):
        self.head = Node(val, self.head)
        #store head val
        #insert val at head
        #point new val next at prev head



    def pop(self):
        oldHead = self.head
        self.head = self.head.next
        return oldHead

        #get head
        #update head to old head.next
        #return old head


    def size(self):
        counter = 0
        pointer = self.head

        if pointer:
            counter += 1

            while pointer.next:
                pointer = pointer.next
                counter += 1

        return counter

        #start at head
        #loop through with counter

    def search(self, val):
        pass
        #start at head
        #check each item for equality

    def remove(self, node):
        pass
        #start at head, if first, update .next to head
        #loop through till you find in node.next
        #update node.next to node.next.next


    #def print(self)

class Node(object):

    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode
