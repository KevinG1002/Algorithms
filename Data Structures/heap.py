import sys
from this import d


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

    def parent(self, pos) -> int:
        """
        Returns the idx of the parent associated with the node at position "pos"
        """
        parent_idx = pos // 2
        return parent_idx

    def isLeaf(self, pos) -> bool:
        """
        Returns boolean indicating whether the node is a leaf or not. This can be determined by
        """
        if self.leftChild(pos) >= len(self.Heap) or self.rightChild(pos) >= len(
            self.Heap
        ):
            return True
        return False

    def leftChild(self, pos) -> int:
        """
        Given a node in position "pos", returns the position of its left child.
        """
        return 2 * pos

    def rightChild(self, pos) -> int:
        """
        Given a node in position "pos", returns the position of its right child.
        """
        return (2 * pos) + 1

    def maxHeapify(self, pos) -> None:
        """
        Function that maxheapifies a node in the position "pos".
        Ensures that the given node is smaller than its parent as a minimal property, and that it is greater than its children.
        """
        if not self.isLeaf(pos):
            if (
                self.Heap[pos] < self.Heap[self.leftChild(pos)]
                or self.Heap[pos] < self.Heap[self.rightChild(pos)]
            ):

                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.nodeSwap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                else:
                    self.nodeSwap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

        else:
            if self.Heap[pos] > self.Heap[self.parent(pos)]:
                self.maxHeapify(self.parent(pos))

    def nodeSwap(self, pos_node_1, pos_node_2):
        self.Heap[pos_node_1], self.Heap[pos_node_2] = (
            self.Heap[pos_node_2],
            self.Heap[pos_node_1],
        )

    def insert(self, element):
        if self.current_size >= self.max_size:
            raise Exception(
                "Heap has already reached max size. Cannot add new element."
            )
        self.current_size += 1
        self.Heap[self.current_size] = element

        curr_idx = self.current_size

        while self.Heap[curr_idx] > self.Heap[self.parent(curr_idx)]:
            self.nodeSwap(curr_idx, self.parent(curr_idx))
            curr_idx = self.parent(curr_idx)

    def print_tree(self):
        print(self.Heap)
        for i in range(1, (self.current_size // 2) + 1):
            print(
                "PARENT : "
                + str(self.Heap[i])
                + "\tLEFT CHILD : "
                + str(self.Heap[(2 * i)])
                + "\tRIGHT CHILD : "
                + str(self.Heap[(2 * i) + 1])
            )

    def get_max(self):
        popped_item = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.current_size]
        self.current_size -= 1
        self.maxHeapify(self.FRONT)
        print("\n")
        self.print_tree()
        return popped_item


class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.FRONT = 1
        self.current_size = 0
        self.Heap = [0] * (max_size + 1)
        self.Heap[0] = -sys.maxsize

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if (
            self.leftChild(pos) > self.current_size
            or self.rightChild(pos) > self.current_size
        ):
            return True
        return False

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (
                self.Heap[pos] > self.Heap[self.leftChild(pos)]
                or self.Heap[pos] > self.Heap[self.rightChild(pos)]
            ):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swapItem(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swapItem(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
        else:
            if self.Heap[pos] < self.Heap[self.parent(pos)]:
                self.swapItem(pos, self.parent(pos))
                self.minHeapify(self.parent(pos))

    def insert(self, item):
        assert self.current_size <= self.max_size, "Max size reached. Can't add items"
        self.current_size += 1
        self.Heap[self.current_size] = item

        current_pos = self.current_size
        while self.Heap[current_pos] < self.Heap[self.parent(current_pos)]:
            self.swapItem(current_pos, self.parent(current_pos))
            current_pos = self.parent(current_pos)

    def swapItem(self, item_1_pos, item_2_pos):
        self.Heap[item_1_pos], self.Heap[item_2_pos] = (
            self.Heap[item_2_pos],
            self.Heap[item_1_pos],
        )

    def print_tree(self):
        print(self.Heap)
        for i in range(1, (self.current_size // 2) + 1):
            print(
                "Parent: ",
                self.Heap[i],
                "\tLeft Child: ",
                self.Heap[(2 * i)],
                "\tRight Child: ",
                self.Heap[(2 * i) + 1],
            )

    def get_min_item(self):
        min_item = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.current_size]
        self.current_size -= 1
        self.minHeapify(self.FRONT)
        print("\n")
        self.print_tree()
        return min_item


def max_heap_demo():

    heap = MaxHeap(13)
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)
    heap.insert(9)
    heap.insert(10)
    heap.insert(4.5)
    heap.insert(-1)
    heap.print_tree()

    max_item = heap.get_max()
    print("Max item: " + str(max_item))


def min_heap_demo():
    heap = MinHeap(13)
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)
    heap.insert(9)
    heap.insert(10)
    heap.insert(4.5)
    heap.insert(-1)
    heap.print_tree()

    print(heap.get_min_item())


if __name__ == "__main__":
    # min_heap_demo()
    max_heap_demo()
