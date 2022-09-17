def right_rotate(parent):
    left_child = parent.left
    sub_tree = left_child.right
    grandparent = parent.parent

    left_child.right = parent
    left_child.parent = grandparent
    parent.left = sub_tree
    parent.parent = left_child
    if sub_tree is not None:
        sub_tree.parent = parent
    if grandparent is not None and grandparent.left == parent:
        grandparent.left = left_child
    if grandparent is not None and grandparent.right == parent:
        grandparent.right = left_child


def left_rotate(parent):
    right_child = parent.right
    sub_tree = right_child.left
    grandparent = parent.parent

    right_child.left = parent
    right_child.parent = grandparent
    parent.right = sub_tree
    parent.parent = right_child
    if sub_tree is not None:
        sub_tree.parent = parent
    if grandparent is not None and grandparent.left == parent:
        grandparent.left = right_child
    if grandparent is not None and grandparent.right == parent:
        grandparent.right = right_child
