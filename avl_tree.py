from __future__ import annotations
from rotation import right_rotate, left_rotate


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        if self.parent is not None:
            left_height = self.parent.left.height if self.parent.left is not None else -1
            right_height = self.parent.right.height if self.parent.right is not None else -1
            res = "\t" * (max(left_height, right_height)) + self.value.__str__() + f"({self.height})" + "\n"
        else:
            res = "\t" * self.height + self.value.__str__() + f"({self.height})" + "\n"
        if self.left is not None and self.right is not None:
            res += self.left.__str__()
            res += self.right.__str__()
        elif self.left is None and self.right is not None:
            res += "\t" * self.right.height + "None" + "\n"
            res += self.right.__str__()
        elif self.left is not None and self.right is None:
            res += self.left.__str__()
            res += "\t" * self.left.height + "None" + "\n"
        return res

    def __repr__(self):
        return f"Node({self.value})"


class AVLTree:
    def __init__(self, root: Node = None):
        self.root = root

    def __balance_ancestors_height(self, parent: Node):
        while parent is not None:
            left_height = parent.left.height if parent.left is not None else -1
            right_height = parent.right.height if parent.right is not None else -1
            parent.height = max(left_height, right_height) + 1
            parent = parent.parent

    def __get_balance_factor(self, node: Node) -> int:
        left_height = node.left.height if node.left is not None else -1
        right_height = node.right.height if node.right is not None else -1
        return left_height - right_height

    def __unbalanced_insert(self, value: int) -> Node:
        if value is None:
            raise ValueError("Can`t insert empty node")
        else:
            if self.root is None:
                self.root = Node(value)
                return self.root
            else:
                temp = self.root
                while True:
                    if temp.value == value:
                        raise ValueError("Can`t insert duplicate")
                    elif temp.value > value:
                        if temp.left is None:
                            temp.left = Node(value)
                            temp.left.parent = temp
                            self.__balance_ancestors_height(temp.left)
                            return temp.left
                        else:
                            temp = temp.left
                    else:
                        if temp.right is None:
                            temp.right = Node(value)
                            temp.right.parent = temp
                            self.__balance_ancestors_height(temp.right)
                            return temp.right
                        else:
                            temp = temp.right

    def insert(self, value: int):
        node = self.__unbalanced_insert(value)
        parent = node.parent
        if parent is not None:
            grandparent = parent.parent
            while grandparent is not None:
                if self.__get_balance_factor(grandparent) > 1:
                    if grandparent.left is not None and grandparent.left == parent:
                        if parent.left == node:
                            right_rotate(grandparent)
                            if grandparent == self.root:
                                self.root = parent
                        elif parent.right == node:
                            left_rotate(parent)
                            right_rotate(grandparent)
                            if grandparent == self.root:
                                self.root = node
                if self.__get_balance_factor(grandparent) < -1:
                    if grandparent.right is not None and grandparent.right == parent:
                        if parent.right == node:
                            left_rotate(grandparent)
                            if grandparent == self.root:
                                self.root = parent
                        elif parent.left == node:
                            right_rotate(parent)
                            left_rotate(grandparent)
                            if grandparent == self.root:
                                self.root = node
                self.__balance_ancestors_height(node)
                self.__balance_ancestors_height(parent)
                self.__balance_ancestors_height(grandparent)
                node = node.parent
                if node is not None:
                    parent = node.parent
                    if parent is not None:
                        grandparent = parent.parent
                    else:
                        grandparent = None
                else:
                    parent = None
                    grandparent = None

    def print_tree(self):
        print(self.root.__str__())
