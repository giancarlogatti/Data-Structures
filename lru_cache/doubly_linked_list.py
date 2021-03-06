"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_head = ListNode(value, next = self.head)
        if self.length >= 1:
            self.head.prev = new_head #adjust old head back pointer        
            self.tail.prev = new_head

        self.head = new_head
        self.length += 1
        if self.length == 1:
            self.tail = self.head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head != None:
            value = self.head.value
            if self.head.next != None:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
            self.length -= 1
            if self.length == 0:
                self.tail = self.head

            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_tail = ListNode(value, prev = self.tail)
        if self.length >= 1:
            self.tail.next = new_tail
            self.head.prev = new_tail
        self.tail = new_tail
        self.length += 1
        if self.length == 1:
            self.head = self.tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail != None:
            value = self.tail.value
            if self.tail.prev != None:                
                self.tail = self.tail.prev
                self.tail.prev.next = None
            else:
                self.tail = None
            self.length -= 1
            if self.length == 0:
                self.head = self.tail
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length > 0:
            if node == self.head:
                self.remove_from_head()
            elif node == self.tail:
                self.remove_from_tail()
            else: 
                node.prev.next = node.next
                node.next.prev = node.prev 
                self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        node = self.head
        max = float('-inf')
        while node != None:
            if node.value > max:
                max = node.value
            node = node.next

        return max
