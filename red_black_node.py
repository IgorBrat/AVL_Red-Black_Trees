from node import Node
from color import Color


class RedBlackNode(Node):
    def __init__(self, value: int):
        super().__init__(value)
        self.color = Color.BLACK

    def __str__(self, level=0):
        res = ""
        if self.value != 0:
            if self.left is not None and self.right is not None:
                res += self.left.__str__(level + 1)
                res += "\t" * level + f"-> {self.value.__str__()}({self.color.value})\n"
                res += self.right.__str__(level + 1)
            elif self.left is not None and self.right is None:
                res += self.left.__str__(level + 1)
                res += "\t" * level + f"-> {self.value.__str__()}({self.color.value})\n"
                res += "\t" * (level + 1) + "-> " + "None(black)" + "\n"
            elif self.left is None and self.right is not None:
                res += "\t" * (level + 1) + "-> " + "None(black)" + "\n"
                res += "\t" * level + f"-> {self.value.__str__()}({self.color.value})\n"
                res += self.right.__str__(level + 1)
            else:
                res += "\t" * level + f"-> {self.value.__str__()}({self.color.value})\n"
        return res

    def __repr__(self):
        return f"Node({self.value})"
