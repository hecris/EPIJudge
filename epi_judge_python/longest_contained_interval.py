from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    unprocessed = set(A)
    max_length = 0
    while unprocessed:
        x = unprocessed.pop()
        lo = x - 1
        while lo in unprocessed:
            unprocessed.remove(lo)
            lo -= 1

        hi = x + 1
        while hi in unprocessed:
            unprocessed.remove(hi)
            hi += 1

        max_length = max(max_length, hi - lo - 1)
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
