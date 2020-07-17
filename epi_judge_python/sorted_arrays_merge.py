from typing import List

from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    iterators = [iter(l) for l in sorted_arrays]
    heap = [(next(iterator), i) for i, iterator in enumerate(iterators)]
    heapq.heapify(heap)

    res = []

    while heap:
        val, itr_idx = heapq.heappop(heap)
        res.append(val)
        itr = iterators[itr_idx]
        next_val = next(itr, None)
        if next_val is not None:
            heapq.heappush(heap, (next_val, itr_idx))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
