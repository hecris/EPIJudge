from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def helper(root, depth):
        if not root:
            return (True, depth)
        left_balanced, left_height = helper(root.left, depth+1)
        if not left_balanced:
            return (False, depth)
        right_balanced, right_height = helper(root.right, depth+1)
        if not right_balanced:
            return (False, depth)
        return (abs(left_height - right_height) <= 1, max(left_height, right_height))
    return helper(tree, 0)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
