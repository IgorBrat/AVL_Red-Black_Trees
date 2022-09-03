from red_black_node import RedBlackNode
from case import case_1_resolver, case_2_resolver, case_3_resolver, case_4_resolver
from color import Color


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

    def __get_node_to_delete(self, value: int) -> RedBlackNode:
        if value is None:
            raise ValueError("Can`t delete None")
        if self.root is None:
            raise ValueError("Can`t delete from empty tree")
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            else:
                return temp
        return None

    def __replace(self, old: RedBlackNode, new: RedBlackNode):
        if new is not None:
            new.parent = old.parent
        if old.parent is not None:
            if old.parent.left == old:
                old.parent.left = new
            else:
                old.parent.right = new
        else:
            self.root = new

    def __fix_balance(self, curr_node: RedBlackNode):
        while curr_node != self.root and curr_node.color.value == "black":
            if curr_node == curr_node.parent.left:
                sibling = curr_node.parent.right
                if sibling.color.value == "red":
                    case_1_resolver(curr_node, sibling, "left")
                if sibling.left.color.value == sibling.right.color.value == "black" or (
                        sibling.left is None and sibling.right is None):
                    case_2_resolver(curr_node, sibling)
                elif sibling.right.color.value == "black" or sibling.right is None:
                    case_3_resolver(curr_node, sibling, "left")
                else:
                    case_4_resolver(curr_node, sibling, "left")
                    curr_node = self.root
            else:
                sibling = curr_node.parent.left
                if sibling.color.value == "red":
                    case_1_resolver(curr_node, sibling, "right")
                if sibling.left.color.value == sibling.right.color.value == "black":
                    case_2_resolver(curr_node, sibling)
                elif sibling.left.color.value == "black":
                    case_3_resolver(curr_node, sibling, "right")
                else:
                    case_4_resolver(curr_node, sibling, "right")
                    curr_node = self.root
            curr_node.color = Color.BLACK

    def delete(self, value: int):
        node_to_delete = self.__get_node_to_delete(value)
        if node_to_delete is None:
            raise ValueError("No such node in the tree")
        original_color = node_to_delete.color
        if node_to_delete.left is None:
            curr_child = node_to_delete.right
            curr_child.parent = node_to_delete.parent
            self.__replace(node_to_delete, curr_child)
        elif node_to_delete.right is None:
            curr_child = node_to_delete.left
            curr_child.parent = node_to_delete.parent
            self.__replace(node_to_delete, curr_child)
        else:
            node_to_replace = node_to_delete.right
            while node_to_replace.left is not None:
                node_to_replace = node_to_replace.left
            original_color = node_to_replace.color
            curr_child = node_to_replace.right
            if node_to_delete.right == node_to_replace:
                curr_child.parent = node_to_replace
            else:
                self.__replace(node_to_replace, node_to_replace.right)
            self.__replace(node_to_delete, node_to_replace)
            node_to_replace.color = original_color

        if original_color.value == "black":
            self.__fix_balance(curr_child)

    def print_tree(self):
        print(self.root.__str__())
