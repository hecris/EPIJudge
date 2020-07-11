from typing import List

from test_framework import generic_test


def reverse(l, lo, hi):
    while lo < hi:
        l[lo], l[hi] = l[hi], l[lo]
        lo += 1
        hi -= 1

# NOTE: I found this pretty hard
def next_permutation(perm: List[int]) -> List[int]:
    prefix_end = len(perm) - 2
    while prefix_end >= 0 and perm[prefix_end] >= perm[prefix_end + 1]:
        prefix_end -= 1

    if prefix_end == -1:
        return []

    smallest = len(perm) - 1
    while perm[smallest] <= perm[prefix_end]:
        smallest -= 1

    perm[smallest], perm[prefix_end] = perm[prefix_end], perm[smallest]
    reverse(perm, prefix_end+1, len(perm)-1)
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
