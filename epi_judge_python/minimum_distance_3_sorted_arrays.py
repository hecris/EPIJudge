from typing import List

from test_framework import generic_test
import bintrees


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:

    tree = bintrees.RBTree()
    iters = [iter(arr) for arr in sorted_arrays]
    for i, itr in enumerate(iters):
        # NOTE: have to pass in a min_id to handle duplicates
        tree.insert((next(itr), i), itr)

    ans = float('inf')
    while True:
        min_info, min_itr = tree.pop_min()
        min_val, min_id = min_info
        max_val = tree.max_key()[0]
        ans = min(ans, max_val - min_val)

        nxt_val = next(min_itr, None)

        if nxt_val is None:
            break

        tree.insert((nxt_val, min_id), min_itr)

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
