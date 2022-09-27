"""The Node of a Binary tree with left and right subtrees and a key and value
    """


class Node:
    def __init__(self, new_key, val):
        self.key = new_key
        self.value = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return "  key={} data={}, left={}, right={}"
        .format(self.key, self.value, self.left == None, self.right == None)
