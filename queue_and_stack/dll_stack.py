import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def peek(self):
        return self.storage.head.value

    def push(self, value):
        return self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
