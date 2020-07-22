from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # book has more intuitive solution, if A[mid] == k then the first
    # occurence of k cannot occur at or after mid + 1
    lo, hi = 0, len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if k <= A[mid]:
            hi = mid-1
        else:
            lo = mid+1

    return lo if 0 <= lo and lo < len(A) and A[lo] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
