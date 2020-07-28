from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    def solution(lo, hi, start, end):
        if lo > hi:
            return None, 0

        root_val = preorder_sequence[lo]
        if not (start <= root_val <= end):
            return None, 0

        root = BstNode(root_val)
        root.left, left_size = solution(lo+1, hi, start, root_val)
        root.right, right_size = solution(lo+left_size+1, hi, root_val, end)
        return root, left_size + right_size + 1


    return solution(0, len(preorder_sequence) - 1, float('-inf'), float('inf'))[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
