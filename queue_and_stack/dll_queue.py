import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #adding elements to back of queue
        return self.storage.add_to_tail(value)
    
    def peek(self):
        return self.storage.head.value

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
