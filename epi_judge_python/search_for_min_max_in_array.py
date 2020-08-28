import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


# NOTE: did it in multiple passes for clarity
def find_min_max(A: List[int]) -> MinMax:
    if len(A) <= 2:
        return MinMax(min(A), max(A))

    candidates_min = []
    candidates_max = []

    for i in range(0, len(A) - 1, 2): # n/2 comparisons
        if A[i] < A[i+1]:
            candidates_min.append(A[i])
            candidates_max.append(A[i+1])
        else:
            candidates_max.append(A[i])
            candidates_min.append(A[i+1])

    if len(A) % 2:
        candidates_max.append(A[-1])
        candidates_min.append(A[-1])

    return MinMax(min(candidates_min), max(candidates_max)) # 2(n/2 - 1) comparisons, for a total of ~3n/2


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
