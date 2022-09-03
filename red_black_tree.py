from rotation import right_rotate, left_rotate
from red_black_node import RedBlackNode


class RedBlackTree:
    def __init__(self, root: RedBlackNode = None):
        self.root = root

    def print_tree(self, level=0):
        node = self.root
        res = ""

