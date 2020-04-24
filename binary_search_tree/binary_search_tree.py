from collections import deque
from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Recursive insert implementation
    # does not return anything when executed
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes i.e. need to exist
        # for us to call 'insert' on them
        if value < self.value:
            # check is self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if node contains value
        if self.value == target:
            return True
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def recursive_for_each(self, cb):
        # apply the callback
        cb(self.value)
        # base case - node has no children

        # call the cb on the children of this node
        # check that this node has children
        if self.left:
            self.for_each(cb)
        if self.right:
            self.for_each(cb)

    def iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists first(only to get the same results as the recursive approach)
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack
        # breadth-first : queue
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

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
