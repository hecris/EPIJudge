from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    res = []
    if not tree:
        return res

    prev = BinaryTreeNode() # dummy node
    cur = tree
    left = True
    while cur:
        if left:
            while cur.left:
                cur = cur.left
            left = False
        else:
            if cur.right is not prev:
                res.append(cur.data)

            if cur.right is not prev and cur.right:
                cur = cur.right
                left = True
            else:
                cur, prev = cur.parent, cur

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
