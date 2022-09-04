from red_black_tree import RedBlackTree
from color import Color


def main():
    tree = RedBlackTree()
    # tree.unbalanced_insert(20, Color.BLACK)
    # tree.unbalanced_insert(6, Color.RED)
    # tree.unbalanced_insert(30, Color.RED)
    # tree.unbalanced_insert(3, Color.BLACK)
    # tree.unbalanced_insert(9, Color.BLACK)
    # tree.unbalanced_insert(8, Color.RED)
    # tree.unbalanced_insert(10, Color.RED)
    # tree.unbalanced_insert(25, Color.BLACK)
    # tree.unbalanced_insert(40, Color.BLACK)
    # tree.unbalanced_insert(27, Color.RED)
    # tree.delete(6)
    # tree.delete(3)
    # tree.delete(8)
    # tree.delete(20)
    # tree.delete(40)
    tree.unbalanced_insert(55, Color.BLACK)
    tree.unbalanced_insert(40, Color.BLACK)
    tree.unbalanced_insert(65, Color.RED)
    tree.unbalanced_insert(60, Color.BLACK)
    tree.unbalanced_insert(75, Color.BLACK)
    tree.unbalanced_insert(57, Color.RED)
    tree.delete(40)
    tree.print_tree()


if __name__ == '__main__':
    main()
