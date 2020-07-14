import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    def helper(root):
        if not root:
            return root, False

        left, left_is_lca = helper(root.left)
        right, right_is_lca = helper(root.right)

        if root is node0:
            is_lca = left is node1 or right is node1
            return root, is_lca

        if root is node1:
            is_lca = right is node0 or right is node0
            return root, is_lca

        if left is None or right is None:
            return (left, True) if right is None else (right, True)

        return root, True

    return helper(tree)[0]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
