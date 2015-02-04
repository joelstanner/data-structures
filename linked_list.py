class LinkedList(object):
    """docstring for LinkedList"""


    def __init__(self, arg):
        super(LinkedList, self).__init__()
        self.arg = arg
   

    def __str__(self):


    def insert (self, val):
        self.head = new Node(self.head, val)
        #store head val
        #insert val at head
        #point new val next at prev head



    def pop (self):
        oldHead = self.head
        self.head = self.head.next
        return oldHead

        #get head
        #update head to old head.next
        #return old head


    def size (self):
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
        #start at head
        #check each item for equality

    def remove(self, node):
        #start at head, if first, update .next to head
        #loop through till you find in node.next
        #update node.next to node.next.next


    #def print(self)

class Node(object):

    def __init__(self, nextNode=None, val):
        self.val = val
        self.next = nextNode
