import sys
import signal


class TrieNode:
    """
    Node class for the trie data structure
    Taken from https://albertauyeung.github.io/2020/06/15/python-trie.html/
    """

    def __init__(self, char):
        self.char = char  # character stored in this node
        self.is_end = False  # attribute denoting if this character is the end of a word
        self.counter = 0  # counter indicating the number of times a word is inserted (can help us triage words according to their popularity)
        self.children = (
            {}
        )  # dictionary containing child nodes; keys are characters, values are nodes.


class Trie(object):
    """
    Class for the Trie data structure which is composed of Trie Nodes.
    """

    def __init__(self):
        """
        The Trie data structure needs at least the root node.
        The root node, itself, is an empty string.
        """
        self.root = TrieNode("")

    def insert(self, word):
        """
        Class method that inserts a word into the tree
        """
        node = self.root

        # Loop over every character in word. Check if there is no child containig the character, otherwise create a new node.
        for char in word:
            if char in node.children:
                node = node.children[
                    char
                ]  # assign current node as child of root that matches character.

            else:
                # If character not found, create a new node in the trie.
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word once you've iterated through all characters in the word.
        node.is_end = True

        # Increment the counter belonging to the node to indicate that we've visited the node once more.
        node.counter += 1

    def DFS(self, node: TrieNode, prefix: str):
        """
        Depth-First Traversal of the trie data structure
        Args:
            - node: the node we start from
            - prefix: the current prefix to trace a word while traversing the trie.
        """
        # Recursively run this method until you read a word's end.
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.DFS(child, prefix + node.char)

    def query(self, prefix):
        """
        Given an input prefix, retrieve all words stored in the trie
        with that prefix then sort the words that result according to their
        respective counters.
        """

        self.output = []
        node = self.root

        # Verify that the prefix is in the try
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []  # Outcome if prefix not found (return empty list)

        print(prefix[:-1])
        self.DFS(
            node, prefix[:-1]
        )  # Traverse the trie to get all candidates (DFS populates output list)

        return sorted(
            self.output, key=lambda x: x[1], reverse=True
        )  # Sort in descending order


def trie_demo():
    t = Trie()

    while True:
        try:
            new_word = input("Enter your new word: ")
            t.insert(new_word)
        except KeyboardInterrupt:
            print(t.query("ha"))
            sys.exit()


if __name__ == "__main__":
    trie_demo()
