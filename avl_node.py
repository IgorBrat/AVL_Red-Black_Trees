from node import Node


class AVLNode(Node):
    def __init__(self, value: int):
        super().__init__(value)
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
