from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    lo, hi = 0, len(A) - 1
    # base case, lo == hi means interval is length 1
    # which means the minimum element is at lo
    while lo < hi:
        mid = (lo + hi) // 2
        if A[mid] < A[hi]:
            hi = mid
        else:
            lo = mid+1

    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
