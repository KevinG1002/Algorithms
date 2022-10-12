from platform import node
from tokenize import Single


class LL(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def print_inverted_list(self):
        assert self.head is not None, "Empty linked list"
        assert hasattr(self.head, "prev"), "This is not a double linked list"
        curr = self.head
        tail = None
        while curr.next is not None:
            curr = curr.next
        tail = curr
        temp = tail
        while temp is not None:
            print(temp.data)
            temp = temp.prev


class SingleLLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleLLNode(SingleLLNode):
    def __init__(self, data):
        super(DoubleLLNode, self).__init__(data)
        self.prev = None


def single_ll_demo():
    single_ll = LL()

    node_2 = SingleLLNode("my")
    node_3 = SingleLLNode("name")
    node_4 = SingleLLNode("is")
    node_5 = SingleLLNode("Kevin")
    single_ll.head = SingleLLNode("Hello")
    single_ll.head.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    single_ll.print_list()


def double_ll_demo():
    double_ll = LL()
    double_ll.head = DoubleLLNode("To")
    node_2 = DoubleLLNode("be")
    node_3 = DoubleLLNode("or")
    node_4 = DoubleLLNode("not")
    node_5 = DoubleLLNode("to")
    node_6 = DoubleLLNode("be")

    double_ll.head.next = node_2
    node_2.next = node_3
    node_2.prev = double_ll.head
    node_3.next = node_4
    node_3.prev = node_2
    node_4.next = node_5
    node_4.prev = node_3
    node_5.next = node_6
    node_5.prev = node_4
    node_6.prev = node_5

    double_ll.print_list()
    print("\n")
    double_ll.print_inverted_list()


if __name__ == "__main__":
    # single_ll_demo()
    double_ll_demo()
