from typing import Iterator, List

from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    res = []
    heap = [next(sequence) for _ in range(k)]
    heapq.heapify(heap)

    val = next(sequence, None)
    while heap:
        if val is not None:
            res.append(heapq.heappushpop(heap, val))
            val = next(sequence, None)
        else:
            res.append(heapq.heappop(heap))

    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
