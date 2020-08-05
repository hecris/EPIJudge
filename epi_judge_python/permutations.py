from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def solution(lo):
        if lo == len(A):
            res.append(A.copy())
            return

        for i in range(lo, len(A)):
            A[lo], A[i] = A[i], A[lo]
            solution(lo+1)
            A[lo], A[i] = A[i], A[lo]

    res = []
    solution(0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
