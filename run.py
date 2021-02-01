from util.Node import Node


def func_inorder(func, node):
    if node:
        func_inorder(func, node.left)
        func(node.value)
        func_inorder(func, node.right)


def func_postorder(func, node):
    if node:
        func_postorder(func, node.left)
        func_postorder(func, node.right)
        func(node.value)


def func_preorder(func, node):
    if node:
        func(node.value)
        func_preorder(func, node.left)
        func_preorder(func, node.right)


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
    inorder = []
    print(func_inorder)
    func_inorder(inorder.append, root)
    print(inorder)

    # Good for removing leaves first
    postorder = []
    print(func_postorder)
    func_postorder(postorder.append, root)
    print(postorder)

    # Good for showing tranversal of b-tree starting left
    preorder = []
    print(func_preorder)
    func_preorder(preorder.append, root)
    print(preorder)
