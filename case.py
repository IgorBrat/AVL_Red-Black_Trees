from red_black_node import RedBlackNode
from color import Color
from rotation import right_rotate, left_rotate


def case_1_resolver(curr_node: RedBlackNode, sibling: RedBlackNode, curr_node_is: str):
    if curr_node_is == "left":
        curr_node.parent.right.color = Color.BLACK
        curr_node.parent.color = Color.RED
        left_rotate(curr_node.parent)
        sibling = curr_node.parent.right
    if curr_node_is == "right":
        curr_node.parent.left.color = Color.BLACK
        curr_node.parent.color = Color.RED
        right_rotate(curr_node.parent)
        sibling = curr_node.parent.left


def case_2_resolver(curr_node: RedBlackNode, sibling: RedBlackNode):
    sibling.color = Color.RED
    curr_node = curr_node.parent


def case_3_resolver(curr_node: RedBlackNode, sibling: RedBlackNode, curr_node_is: str):
    if curr_node_is == "left":
        if sibling.left is not None:
            sibling.left.color.value = Color.BLACK
        sibling.color = Color.RED
        right_rotate(sibling)
        sibling = curr_node.parent.right
    if curr_node_is == "right":
        if sibling.right is not None:
            sibling.right.color.value = Color.BLACK
        sibling.color = Color.RED
        left_rotate(sibling)
        sibling = curr_node.parent.left


def case_4_resolver(curr_node: RedBlackNode, sibling: RedBlackNode, curr_node_is: str):
    if curr_node_is == "left":
        sibling.color = curr_node.parent.color
        curr_node.parent.color = Color.BLACK
        if sibling.right is not None:
            sibling.right.color = Color.BLACK
        left_rotate(curr_node.parent)
    if curr_node_is == "right":
        sibling.color = curr_node.parent.color
        curr_node.parent.color = Color.BLACK
        if sibling.left is not None:
            sibling.left.color = Color.BLACK
        right_rotate(curr_node.parent)
