from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    indices = {x: i for i, x in enumerate(inorder)}

    def helper(plo, phi, ilo, ihi):
        if plo >= phi or ilo >= ihi:
            return None

        root_val = preorder[plo]
        root_index = indices[root_val]
        left_size = root_index - ilo
        root = BinaryTreeNode(root_val)
        root.left = helper(plo+1, plo+1+left_size, ilo, root_index)
        root.right = helper(plo+1+left_size, phi, root_index+1, ihi)
        return root

    return helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
