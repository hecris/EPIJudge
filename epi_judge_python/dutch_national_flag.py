import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    '''
    0 1 2 0 2 1 1, index = 1, n = 1
    0 1 1 0 1 2 2

    1. hi, go until reach x != n
    2. lo, go until reach x == n

    0 1 2 0 2 1 1, n = 2
        i       j
    0 1 1 0 2 1 2
          i   j

    0 1 1 2, n = 1

    '''

    lo, hi = 0, len(A) - 1
    n = A[pivot_index]
    while True:
        while lo < len(A) and A[lo] <= n:
            lo += 1

        while hi >= 0 and A[hi] > n:
            hi -= 1

        if lo >= hi:
            break

        A[lo], A[hi] = A[hi], A[lo]
        lo += 1
        hi -= 1

    upper = hi
    lo = 0
    while True:
        while lo < upper and A[lo] != n:
            lo += 1

        while hi >= 0 and A[hi] == n:
            hi -= 1

        if lo >= hi:
            break

        A[lo], A[hi] = A[hi], A[lo]
        lo += 1
        hi -= 1

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
