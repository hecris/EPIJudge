import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
import functools

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    miss_xor_dup = functools.reduce(lambda value, i: value ^ i[0] ^ i[1], enumerate(A), 0)
    # find leftmost differing bit between miss and dup
    # this is equivalent to the leftmost set bit in miss ^ dup
    # a property of XOR!
    diff_bit = (miss_xor_dup & ~(miss_xor_dup - 1))
    miss_or_dup = 0
    for i in range(len(A)):
        if i & diff_bit:
            miss_or_dup ^= i

        if A[i] & diff_bit:
            miss_or_dup ^= A[i]

    if miss_or_dup in A:
        return DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_xor_dup)

    return DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
