from red_black_node import RedBlackNode
from color import Color


class RedBlackTree:
    def __init__(self, root: RedBlackNode = None):
        self.Null = RedBlackNode(0)
        self.Null.left = None
        self.Null.right = None
        self.root = root if root is not None else self.Null

    def unbalanced_insert(self, value: int, color: Color) -> RedBlackNode:
        if value is None:
            raise ValueError("Can`t insert empty node")
        else:
            if self.root == self.Null:
                self.root = RedBlackNode(value)
                self.root.left = self.Null
                self.root.right = self.Null
                self.root.color = color
                return self.root
            else:
                temp = self.root
                while True:
                    if temp.value == value:
                        raise ValueError("Can`t insert duplicate")
                    elif temp.value > value:
                        if temp.left is self.Null:
                            temp.left = RedBlackNode(value)
                            temp.left.left = self.Null
                            temp.left.right = self.Null
                            temp.left.color = color
                            temp.left.parent = temp
                            return temp.left
                        else:
                            temp = temp.left
                    else:
                        if temp.right is self.Null:
                            temp.right = RedBlackNode(value)
                            temp.right.left = self.Null
                            temp.right.right = self.Null
                            temp.right.color = color
                            temp.right.parent = temp
                            return temp.right
                        else:
                            temp = temp.right

    def __get_node_to_delete(self, value: int) -> RedBlackNode:
        if value is None:
            raise ValueError("Can`t delete None")
        if self.root == self.Null:
            raise ValueError("Can`t delete from empty tree")
        temp = self.root
        while temp != self.Null:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            else:
                return temp
        return temp

    def __replace(self, old: RedBlackNode, new: RedBlackNode):
        if old.parent is None:
            self.root = new
        else:
            if old.parent.left == old:
                old.parent.left = new
            else:
                old.parent.right = new
        new.parent = old.parent

    def __fix_balance(self, curr_node: RedBlackNode):
        while curr_node != self.root and curr_node.color.value == "black":
            if curr_node == curr_node.parent.left:
                sibling = curr_node.parent.right
                if sibling.color.value == "red":
                    sibling = self.case_1_resolver(curr_node, sibling, "left")
                if sibling.left.color.value == sibling.right.color.value == "black":
                    sibling.color = Color.RED
                    curr_node = curr_node.parent
                elif sibling.right.color.value == "black":
                    self.case_3_resolver(sibling, "left")
                    sibling = curr_node.parent.right
                else:
                    self.case_4_resolver(curr_node, sibling, "left")
                    curr_node = self.root
            else:
                sibling = curr_node.parent.left
                if sibling.color.value == "red":
                    sibling = self.case_1_resolver(curr_node, sibling, "right")
                if sibling.left.color.value == sibling.right.color.value == "black":
                    sibling.color = Color.RED
                    curr_node = curr_node.parent
                elif sibling.left.color.value == "black":
                    self.case_3_resolver(sibling, "right")
                    sibling = curr_node.parent.left
                else:
                    self.case_4_resolver(curr_node, sibling, "right")
                    curr_node = self.root
        curr_node.color = Color.BLACK

    def delete(self, value: int):
        node_to_delete = self.__get_node_to_delete(value)
        if node_to_delete is None:
            raise ValueError("No such node in the tree")
        original_color = node_to_delete.color
        if node_to_delete.left == self.Null:
            curr_child = node_to_delete.right
            self.__replace(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.Null:
            curr_child = node_to_delete.left
            self.__replace(node_to_delete, node_to_delete.left)
        else:
            node_to_replace = node_to_delete.right
            while node_to_replace.left != self.Null:
                node_to_replace = node_to_replace.left
            original_color = node_to_replace.color
            curr_child = node_to_replace.right
            if node_to_replace.parent == node_to_delete:
                curr_child.parent = node_to_replace
            else:
                self.__replace(node_to_replace, node_to_replace.right)
                node_to_replace.right = node_to_delete.right
                node_to_replace.right.parent = node_to_replace
            self.__replace(node_to_delete, node_to_replace)
            node_to_replace.left = node_to_delete.left
            node_to_replace.left.parent = node_to_replace
            node_to_replace.color = node_to_delete.color

        if original_color.value == "black":
            self.__fix_balance(curr_child)

    def print_tree(self):
        print(self.root.__str__())

    def right_rotate(self, parent):
        left_child = parent.left
        grandparent = parent.parent
        parent.left = left_child.right
        if left_child.right != self.Null:
            left_child.right.parent = parent
        left_child.parent = grandparent
        if grandparent is None:
            self.root = left_child
        elif parent == grandparent.right:
            grandparent.right = left_child
        else:
            grandparent.left = left_child
        left_child.right = parent
        parent.parent = left_child

    def left_rotate(self, parent: RedBlackNode):
        right_child = parent.right
        grandparent = parent.parent
        parent.right = right_child.left
        if right_child.left != self.Null:
            right_child.left.parent = parent
        right_child.parent = grandparent
        if grandparent is None:
            self.root = right_child
        elif parent == grandparent.left:
            grandparent.left = right_child
        else:
            grandparent.right = right_child
        right_child.left = parent
        parent.parent = right_child

    def case_1_resolver(self, curr_node: RedBlackNode, sibling: RedBlackNode, curr_node_is: str):
        sibling.color = Color.BLACK
        curr_node.parent.color = Color.RED
        if curr_node_is == "left":
            self.left_rotate(curr_node.parent)
            sibling = curr_node.parent.right
        if curr_node_is == "right":
            self.right_rotate(curr_node.parent)
            sibling = curr_node.parent.left
        return sibling

    def case_3_resolver(self, sibling: RedBlackNode, curr_node_is: str):
        sibling.color = Color.RED
        if curr_node_is == "left":
            sibling.left.color = Color.BLACK
            self.right_rotate(sibling)
        if curr_node_is == "right":
            sibling.right.color = Color.BLACK
            self.left_rotate(sibling)

    def case_4_resolver(self, curr_node: RedBlackNode, sibling: RedBlackNode, curr_node_is: str):
        sibling.color = curr_node.parent.color
        curr_node.parent.color = Color.BLACK
        sibling.right.color = Color.BLACK
        if curr_node_is == "left":
            sibling.right.color = Color.BLACK
            self.left_rotate(curr_node.parent)
        if curr_node_is == "right":
            sibling.left.color = Color.BLACK
            self.right_rotate(curr_node.parent)
