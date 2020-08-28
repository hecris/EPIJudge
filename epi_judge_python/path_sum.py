from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def solution(root, weight):
        if not root:
            return False

        if not root.left and not root.right:
            return weight == root.data

        remain = weight - root.data
        return solution(root.left, remain) or solution(root.right, remain)

    return solution(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
