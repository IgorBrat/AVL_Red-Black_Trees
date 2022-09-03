from red_black_tree import RedBlackTree
from color import Color


def main():
    tree = RedBlackTree()
    tree.unbalanced_insert(10)
    tree.unbalanced_insert(11)
    tree.unbalanced_insert(2)
    tree.unbalanced_insert(3)
    tree.unbalanced_insert(20)
    tree.unbalanced_insert(1)
    tree.unbalanced_insert(15)
    tree.unbalanced_insert(30)
    tree.unbalanced_insert(40)
    tree.unbalanced_insert(18)
    tree.unbalanced_insert(17)
    tree.print_tree()


if __name__ == '__main__':
    main()
