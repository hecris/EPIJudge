from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    lo, hi = 0, 0
    indices = {}
    max_length = 1 if A else 0
    while hi < len(A):
        if A[hi] in indices and indices[A[hi]] >= lo:
            max_length = max(max_length, hi - lo)
            lo = indices[A[hi]] + 1

        indices[A[hi]] = hi
        hi += 1

    max_length = max(max_length, hi - lo)
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
