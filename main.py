from avl_tree import AVLTree


def main():
    tree = AVLTree()
    tree.insert(10)
    tree.insert(11)
    tree.insert(2)
    tree.insert(3)
    tree.insert(20)
    tree.insert(1)
    tree.insert(15)
    tree.insert(30)
    tree.insert(40)
    tree.insert(18)
    tree.insert(17)
    tree.print_tree()


if __name__ == '__main__':
    main()

