import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    # more "recursive" solution
    def alt_solution(root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root]

        return alt_solution(root.left) + alt_solution(root.right)

    # return alt_solution(tree)

    res = []
    if not tree:
        return res

    def dfs(root):
        if not root.left and not root.right:
            res.append(root)
            return

        if root.left:
            dfs(root.left)

        if root.right:
            dfs(root.right)

    dfs(tree)
    return res


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure('Result list can\'t contain None')
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_connect_leaves.py',
                                       'tree_connect_leaves.tsv',
                                       create_list_of_leaves_wrapper))
