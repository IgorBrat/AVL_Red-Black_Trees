from rotation import right_rotate, left_rotate
from red_black_node import RedBlackNode


class RedBlackTree:
    def __init__(self, root: RedBlackNode = None):
        self.root = root

    def unbalanced_insert(self, value: int) -> RedBlackNode:
        if value is None:
            raise ValueError("Can`t insert empty node")
        else:
            if self.root is None:
                self.root = RedBlackNode(value)
                return self.root
            else:
                temp = self.root
                while True:
                    if temp.value == value:
                        raise ValueError("Can`t insert duplicate")
                    elif temp.value > value:
                        if temp.left is None:
                            temp.left = RedBlackNode(value)
                            temp.left.parent = temp
                            return temp.left
                        else:
                            temp = temp.left
                    else:
                        if temp.right is None:
                            temp.right = RedBlackNode(value)
                            temp.right.parent = temp
                            return temp.right
                        else:
                            temp = temp.right

    def print_tree(self):
        print(self.root.__str__())

