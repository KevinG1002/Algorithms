import sys


class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.Heap = [0] * (self.max_size + 1)
        self.Heap[
            0
        ] = (
            sys.maxsize
        )  # sys.maxsize reports the platform's pointer size, and that limits the size of Python's data structures such as strings and lists.
        self.FRONT = 1

    def parent(self, pos):
        """
        Returns the idx of the parent associated with the node at position "pos"
        """
        parent_idx = pos // 2
        return parent_idx

    def isLeaf(self, pos):
        """
        Returns boolean indicating whether the node is a leaf or not. This can be determined by
        """
        if self.leftChild(pos) >= len(self.Heap) or self.rightChild(pos) >= len(
            self.Heap
        ):
            return True
        return False

    def leftChild(self, pos):
        """
        Given a node in position "pos", returns the position of its left child.
        """
        return (2 * pos) + 1

    def rightChild(self, pos):
        """
        Given a node in position "pos", returns the position of its right child.
        """
        return (2 * pos) + 2
    
    def maxHeap(self, pos):
        


class MinHeap:
    def __init__(self):
        pass


class Node(object):
    def __init__(self, data):
        self.data = data
