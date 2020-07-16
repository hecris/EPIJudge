import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # NOTE: cool alternative recursive solution from the book
    def alternate(preorder_iter):
        root = next(preorder_iter)
        if not root:
            return None
        left = alternate(preorder_iter)
        right = alternate(preorder_iter)
        return BinaryTreeNode(root, left, right)

    # return alternate(iter(preorder))

    if preorder[0] is None:
        return None

    root = BinaryTreeNode(preorder[0])
    stack = [[root, 0]]

    for val in preorder[1:]:
        node = None if val is None else BinaryTreeNode(val)
        parent, count = stack[-1]

        if count == 0:
            parent.left = node
        else:
            parent.right = node

        stack[-1][1] += 1

        if stack[-1][1] == 2:
            stack.pop()

        if node:
            stack.append([node, 0])

    return root


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
