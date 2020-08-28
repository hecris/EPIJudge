from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools


def find_missing_element(stream: Iterator[int]) -> int:
    capacity = 1 << 16
    buckets = [0] * capacity
    stream, stream_copy = itertools.tee(stream)
    for num in stream:
        msb = num >> 16
        buckets[msb] += 1

    missing_bucket = next(i for i in range(capacity) if buckets[i] < capacity)
    buckets = [0] * capacity

    for num in stream_copy:
        # NOTE: cool trick to get 16 one's in binary
        lsb = ((1 << 17) - 1) & num
        msb = num >> 16
        if msb == missing_bucket:
            buckets[lsb] += 1

    lsb = next(i for i in range(capacity) if buckets[i] == 0)

    return (missing_bucket << 16) + lsb


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
