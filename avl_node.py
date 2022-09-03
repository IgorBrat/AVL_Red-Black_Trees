from node import Node


class AVLNode(Node):
    def __init__(self, value: int):
        super().__init__(value)
        self.height = 0

    def __str__(self, level=0):
        res = ""
        if self.left is not None and self.right is not None:
            res += self.left.__str__(level + 1)
            res += "\t" * level + "-> " + self.value.__str__() + "\n"
            res += self.right.__str__(level + 1)
        elif self.left is not None and self.right is None:
            res += self.left.__str__(level + 1)
            res += "\t" * level + "-> " + self.value.__str__() + "\n"
            res += "\t" * (level + 1) + "-> " + "None" + "\n"
        elif self.left is None and self.right is not None:
            res += "\t" * (level + 1) + "-> " + "None" + "\n"
            res += "\t" * level + "-> " + self.value.__str__() + "\n"
            res += self.right.__str__(level + 1)
        else:
            res += "\t" * level + "-> " + self.value.__str__() + "\n"
        return res
