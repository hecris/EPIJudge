from typing import List

from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    res = []
    if not A: return res

    heap = [(-A[0], 0)]
    while len(res) < k:
        val, idx = heapq.heappop(heap)
        res.append(-val)
        for child in (idx * 2 + 1, idx * 2 + 2):
            if child < len(A):
                heapq.heappush(heap, (-A[child], child))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
