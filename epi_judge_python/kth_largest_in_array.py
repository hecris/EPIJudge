from typing import List

from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition(A, lo, hi, pivot):
        A[lo], A[pivot] = A[pivot], A[lo]
        i, j = lo, hi
        while i < j:
            while i < hi and A[i] <= A[lo]:
                i += 1

            while j >= lo and A[j] > A[lo]:
                j -= 1

            if i >= j:
                break

            A[i], A[j] = A[j], A[i]

        A[j], A[lo] = A[lo], A[j]
        return j

    lo, hi = 0, len(A) - 1
    while lo <= hi:
        pivot = random.randint(lo, hi)
        idx = partition(A, lo, hi, pivot)
        elements_to_right = len(A) - 1 - idx
        if elements_to_right == k - 1:
            return A[idx]
        elif elements_to_right < k - 1:
            hi = idx - 1
        else:
            lo = idx + 1

    return A[hi]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
