from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    furthest, i = 0, 0
    while i <= furthest and i < len(A):
        furthest = max(furthest, i + A[i])
        i += 1

    return i >= len(A)

def my_can_reach_end(A: List[int]) -> bool:
    target = len(A) - 1
    for i in reversed(range(len(A))):
        if i + A[i] >= target:
            target = i
        i -= 1
    return target == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
