from util.Node import Node


def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node)
        print_inorder(node.right)


def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node)


def print_preorder(node):
    if node:
        print(node)
        print_preorder(node.left)
        print_preorder(node.right)


if __name__ == "__main__":
    import random

    def generate():
        return random.randint(1, 9)

    root = Node()
    root.add(4)
    root.add(2)
    root.add(6)
    root.add(1)
    root.add(3)
    root.add(5)
    root.add(7)

    # Good for sorting by value
    print(print_inorder)
    print_inorder(root)

    # Good for removing leaves first
    print(print_postorder)
    print_postorder(root)

    # Good for showing tranversal of b-tree starting left
    print(print_preorder)
    print_preorder(root)
