import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        while True:
            if value >= node.value:
                if(node.right != None):
                    node = node.right
                else:
                    #needs to be inserted to the right
                    node.right = BinarySearchTree(value)
                    break
            else:
                if(node.left != None):
                    node = node.left
                else:
                    node.left = BinarySearchTree(value)
                    break
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while node != None:
            if target == node.value:
                return True
            else:
                if target > node.value:
                    node = node.right
                else:
                    node = node.left
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        while True:
            if node.right == None:
                return node.value
            node = node.right

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def rec_help(node, cb):
            if node == None:
                return
            node.value = cb(node.value)
            rec_help(node.left, cb)
            rec_help(node.right, cb)
        rec_help(self, cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
