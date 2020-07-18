from typing import Iterator, List

from test_framework import generic_test
import heapq


def online_median(sequence: Iterator[int]) -> List[float]:
    maxh, minh, res = [], [], []
    for num in sequence:
        # adding an element greater than the median will
        # push the median to the lower half
        heapq.heappush(maxh, -heapq.heappushpop(minh, num))
        # adding an element leq than the median will push the
        # median up one position in the upper half
        if len(maxh) > len(minh):
            heapq.heappush(minh, -heapq.heappop(maxh))

        res.append(0.5 * (-maxh[0] + minh[0]) if len(minh) == len(maxh) else minh[0])

    return res

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
