from node import Node


class RedBlackNode(Node):
    def __init__(self, value: int):
        super().__init__(value)
        self.color = 0
