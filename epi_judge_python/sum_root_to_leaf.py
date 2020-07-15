from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# NOTE: there is a way to do this without nonlocal
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    res = 0
    def preorder(root, x):
        nonlocal res
        if not root:
            return

        x = (x << 1) + root.data
        if not root.left and not root.right:
            res += x
            return

        preorder(root.left, x)
        preorder(root.right, x)

    preorder(tree, 0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
