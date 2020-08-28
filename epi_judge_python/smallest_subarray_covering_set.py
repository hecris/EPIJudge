import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import defaultdict

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


# NOTE: this can be solved using HashMap + Doubly Linked List
# which seems like a good technique for many problems as well (LRU cache)
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    matches = defaultdict(int)
    lo, hi = 0, 0
    min_subarray = Subarray(float('-inf'), float('inf'))

    while hi < len(paragraph):
        word = paragraph[hi]
        if word in keywords:
            matches[word] += 1

        if len(matches) == len(keywords):
            while lo < len(paragraph) and (paragraph[lo] not in keywords or len(matches) == len(keywords)):
                if len(matches) == len(keywords):
                    if hi - lo < min_subarray.end - min_subarray.start:
                        min_subarray = Subarray(lo, hi)

                if paragraph[lo] in keywords:
                    matches[paragraph[lo]] -= 1
                    if matches[paragraph[lo]] == 0:
                        del matches[paragraph[lo]]

                lo += 1

        hi += 1

    return min_subarray


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
