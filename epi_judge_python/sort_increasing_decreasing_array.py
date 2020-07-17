from typing import List

from test_framework import generic_test
import heapq


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # make iterators for sorted subarrays
    itrs = []
    start = 0
    increasing = True
    for i in range(len(A) - 1):
        if increasing and not A[i] < A[i+1]:
            itrs.append(iter(range(start, i+1)))
            start = i+1
            increasing = False
        elif not increasing and not A[i] > A[i+1]:
            itrs.append(iter(reversed(range(start, i+1))))
            start = i+1
            increasing = True

    if increasing:
        itrs.append(iter(range(start, len(A))))
    else:
        itrs.append(iter(reversed(range(start, len(A)))))

    # merge k sorted subarrays using the iterators
    heap = [(A[next(itr)], i) for i, itr in enumerate(itrs)]
    heapq.heapify(heap)
    res = []

    while heap:
        val, itr_idx = heapq.heappop(heap)
        itr = itrs[itr_idx]
        res.append(val)
        next_idx = next(itr, None)
        if next_idx is not None:
            heapq.heappush(heap, (A[next_idx], itr_idx))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
