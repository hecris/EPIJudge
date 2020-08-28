from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# NOTE: super cool solution, O(h) space BTW
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    res = []
    if not tree:
        return res

    stack = [(tree, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            res.append(node.data)
        else:
            if node.right:
                stack.append((node.right, False))

            stack.append((node, True))

            if node.left:
                stack.append((node.left, False))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
