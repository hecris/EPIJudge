from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    def is_mirror(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.data == root2.data and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
    return is_mirror(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
