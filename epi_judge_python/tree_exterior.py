import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    left, right, leaves = [], [], []
    if not tree:
        return left

    if not tree.left and not tree.right:
        return [tree]

    # get path to leftmost leaf as well as leaves
    def left_exterior(root, l, left, leaves):
        if l:
            left.append(root)
        elif not root.left and not root.right:
            leaves.append(root)
            return

        if root.left:
            left_exterior(root.left, l, left, leaves)

        if root.right:
            left_exterior(root.right, l and root.left is None, left, leaves)

    left_exterior(tree, tree.left is not None, left, leaves)

    cur = tree
    if cur and cur.right:
        while cur.left or cur.right:
            if cur is not tree:
                right.append(cur)

            if cur.right:
                cur = cur.right
            else:
                cur = cur.left

    right.reverse()
    return (left or [tree]) + leaves + right


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
